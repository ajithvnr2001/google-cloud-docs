---
url: https://docs.cloud.google.com/sql/docs/mysql/release-notes/
title: Cloud SQL for MySQL release notes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:51:09.326944+00:00
---

# Cloud SQL for MySQL release notes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/mysql/release-notes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ MySQL ](https://docs.cloud.google.com/sql/docs/mysql)
  * [ Resources ](https://docs.cloud.google.com/sql/docs/mysql/resources)



Send feedback 

#  Cloud SQL for MySQL release notes Stay organized with collections  Save and categorize content based on your preferences. 

This page documents production updates to Cloud SQL for MySQL. You can check this page for announcements about new or updated features, bug fixes, known issues, and deprecated functionality. 

You can see the latest product updates for all of Google Cloud on the [ Google Cloud](https://docs.cloud.google.com/release-notes) page, browse and filter all release notes in the [Google Cloud console](https://console.cloud.google.com/release-notes), or programmatically access release notes in [BigQuery](https://console.cloud.google.com/bigquery?p=bigquery-public-data&d=google_cloud_release_notes&t=release_notes&page=table). 

To get the latest product updates delivered to you, add the URL of this page to your [feed reader](https://wikipedia.org/wiki/Comparison_of_feed_aggregators), or add the [feed URL](https://docs.cloud.google.com/feeds/cloud-sql-mysql-release-notes.xml) directly. 

## October 14, 2026

Issue

When you enable the [Knowledge Catalog (formerly Dataplex Universal Catalog)](https://docs.cloud.google.com/sql/docs/mysql/dataplex-catalog-integration) integration on a Cloud SQL for MySQL instance created before April 18, 2026, the integration defaults to once a day instead of near real-time.

Near real-time updates upon Knowledge Catalog enablement aren't yet available for all existing instances. A new announcement will be published when this feature becomes available.

## October 13, 2026

Feature

[Private Service Connect](https://docs.cloud.google.com/sql/docs/mysql/about-private-service-connect) is now the default private IP connectivity option when you create a Cloud SQL for MySQL instance in a new Google Cloud project. Private Service Connect lets you connect to your instance from multiple Virtual Private Cloud (VPC) networks across different groups, projects, or organizations, and supports automatic endpoint and DNS record provisioning. When you configure private IP for an instance, you can still choose to use private services access or both connectivity options.

For more information, see [Private IP configuration options](https://docs.cloud.google.com/sql/docs/mysql/private-ip) and [Configure Private Service Connect](https://docs.cloud.google.com/sql/docs/mysql/configure-private-service-connect).

## October 10, 2026

Change

MySQL 8.0.46 is now the [default minor version](https://docs.cloud.google.com/sql/docs/mysql/db-versions#database-version-support) for Cloud SQL for MySQL 8.0.

For more information about minor version support in Cloud SQL for MySQL, see [MySQL 8.0](https://docs.cloud.google.com/sql/docs/mysql/db-versions#mysql-8.0).

## October 09, 2026

Feature

**Note:** Near real-time sync upon Knowledge Catalog (KC) enablement isn't available for existing instances created before April 18, 2026. For more information, see the release note from October 14, 2026. 

When you enable [Knowledge Catalog (formerly Dataplex Universal Catalog)](https://docs.cloud.google.com/sql/docs/mysql/dataplex-catalog-integration) integration on an eligible Cloud SQL for MySQL instance created before April 18, 2026 where the integration is currently turned off, the instance now syncs schema and metadata updates to Knowledge Catalog in near real-time instead of once a day (instances created on or after April 18, 2026 have near real-time sync enabled by default).

This feature is available for instances running MySQL version 8.0 or later on the [new network architecture](https://docs.cloud.google.com/sql/docs/mysql/upgrade-cloud-sql-instance-new-network-architecture#overview). If Knowledge Catalog integration is already enabled on the instance with once-a-day updates, you can [deactivate](https://docs.cloud.google.com/sql/docs/mysql/dataplex-catalog-integration#deactivate-dataplex-catalog) and re-enable the integration to switch to near real-time updates.

For more information, see [Enable the integration of Knowledge Catalog on an existing Cloud SQL instance](https://docs.cloud.google.com/sql/docs/mysql/dataplex-catalog-integration#enable-dataplex-catalog).

## October 08, 2026

Feature

Cloud SQL for MySQL now supports the `innodb_cloudsql_managed_buffer_pool_tuneup_pct` database flag.

Managed buffer pool automatically adjusts the InnoDB buffer pool size to reduce out-of-memory events. When instance memory usage remains at or below 70% for 10 minutes or longer after prior reductions, Cloud SQL increases the buffer pool size. You can now use the `innodb_cloudsql_managed_buffer_pool_tuneup_pct` flag to change this 70% threshold to a different percentage. Increase the threshold to restore the InnoDB buffer pool size when baseline usage exceeds 70%, or decrease it to preserve additional RAM allocation for memory spikes.

This flag requires the Cloud SQL maintenance version [_MYSQL_VERSION_.R20260726.00_05](https://docs.cloud.google.com/sql/docs/mysql/maintenance-changelog) or later. For more information, see [Enable managed buffer pool](https://docs.cloud.google.com/sql/docs/mysql/optimize-high-memory-usage#enable-managed-buffer-pool).

Feature

Cloud SQL for MySQL supports blue-green deployments ([Preview](https://cloud.google.com/products#product-launch-stages)).

Blue-green deployments let you update databases—such as performing major version upgrades from MySQL 8.0 to 8.4 and staging hardware or configuration modifications—while minimizing downtime. During a blue-green deployment, Cloud SQL creates a separate staging environment (green) that mirrors your existing production environment (blue) and maintains continuous logical replication from blue to green. You can test application compatibility and performance on the green environment without affecting production traffic, and then trigger a switchover to the green environment with minimal application downtime.

For more information, see [About blue-green deployments in Cloud SQL](https://docs.cloud.google.com/sql/docs/mysql/about-blue-green-deployments).

## October 06, 2026

Change

Cloud SQL for MySQL now supports up to 100,000 concurrent connections for Private Service Connect enabled instances created on or after September 30, 2026 with 16 or more vCPUs.

For more information, see [Configure Private Service Connect](https://docs.cloud.google.com/sql/docs/mysql/configure-private-service-connect#limitations).

## September 28, 2026

Breaking

To improve security, removed the `cloudsql.instances.export` permission from the following roles:

  * Cloud SQL Viewer (`roles/cloudsql.viewer`)
  * Basic Reader (`roles/reader`)
  * Basic Viewer (Legacy) (`roles/viewer`)



To retain export capabilities, assign the Cloud SQL Editor (`roles/cloudsql.editor`) role or update custom roles to include the `cloudsql.instances.export` permission.

For more information, see [Cloud SQL roles](https://docs.cloud.google.com/sql/docs/mysql/iam-roles).

Change

Cloud SQL for MySQL 9.7.1 is upgraded to MySQL 9.7.2. For more information, see the [MySQL 9.7.2 Release Notes](https://dev.mysql.com/doc/relnotes/mysql/9.7/en/news-9-7-2.html) and [Cloud SQL database versions](https://docs.cloud.google.com/sql/docs/mysql/db-versions).

Change

Cloud SQL for MySQL 8.4.10 is upgraded to MySQL 8.4.11. For more information, see the [MySQL 8.4.11 Release Notes](https://dev.mysql.com/doc/relnotes/mysql/8.4/en/news-8-4-11.html) and [Cloud SQL database versions](https://docs.cloud.google.com/sql/docs/mysql/db-versions).

## September 21, 2026

Feature

The [C4 machine series](https://docs.cloud.google.com/sql/docs/mysql/machine-series-overview#c4) is available for Cloud SQL for MySQL Enterprise Plus instances in the following regions:

  * `asia-east2` — Hong Kong
  * `asia-southeast2` — Jakarta, Indonesia
  * `europe-west3` — Frankfurt, Germany
  * `europe-west4` — Eemshaven, Netherlands
  * `europe-west8` — Milan, Italy
  * `us-east5` — Columbus, Ohio, USA
  * `us-south1` — Dallas, Texas, USA
  * `us-west4` — Las Vegas, Nevada, USA



The C4 machine series provides the following benefits:

  * Supports fifth and sixth generation Intel Xeon Scalable processors.
  * Offers a price-performance balance that makes it suitable for high-demand workloads.



## September 17, 2026

Change

Cloud SQL for MySQL now automatically enables point-in-time recovery (PITR) in a separate, asynchronous operation after disaster recovery (DR) switchover and replica failover operations complete. Because PITR enablement no longer blocks switchover and replica failover, these operations complete faster, helping you reduce your recovery time.

For more information, see [Use advanced disaster recovery (DR)](https://docs.cloud.google.com/sql/docs/mysql/use-advanced-disaster-recovery).

## September 10, 2026

Breaking

Appending `sqlcommenter` tags using the `sql_commenter_enabled` parameter when executing SQL queries on a Cloud SQL remote MCP server is temporarily disabled.

For more information, see [sqlcommenter tags](https://docs.cloud.google.com/sql/docs/mysql/use-cloudsql-mcp#sqlcommenter).

## September 08, 2026

Feature

[Regional endpoints (REP)](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rep) are now generally available ([GA](https://cloud.google.com/products#product-launch-stages)) for the Cloud SQL for MySQL Admin API.

Regional endpoints let you interact with Cloud SQL for MySQL instances using regionalized URLs (such as `sqladmin.[{region}](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rep#supported_regions).rep.googleapis.com`) rather than through a single global endpoint.

Regional endpoints provide regional frontend and load balancing infrastructure that improves data residency by keeping network traffic within the same region as the instance. This reduces the instance's dependency on global frontend infrastructure.

Regional endpoints have strong regional isolation, so the failure of a load balancer or frontend in one region doesn't affect any other region. Regional service load balancers have a separate, regionally isolated control plane.

Regional endpoints are designed to meet stringent data residency and sovereignty standards, such as ITAR and Assured Workloads Regions, ensuring data in transit remains within the committed region.

Certificate management and TLS termination occurs within each region, on the regional load balancer, so data remains encrypted until it reaches its destination region and stays within that region while being processed there.

## September 04, 2026

Feature

The [C4 machine series](https://docs.cloud.google.com/sql/docs/mysql/machine-series-overview#c4) is now available for Cloud SQL for MySQL Enterprise Plus instances in the following regions:

  * `africa-south1` — Johannesburg
  * `asia-northeast3` — Seoul
  * `asia-south2` — Delhi
  * `europe-west6` — Zürich
  * `southamerica-west1` — Santiago
  * `us-west3` — Salt Lake City



The C4 machine series provides the following benefits:

  * Supports fifth and sixth generation Intel Xeon Scalable processors.
  * Offers a price-performance balance that makes it suitable for high-demand workloads.



Feature

Cloud SQL supports in-place upgrades and downgrades to your instance's infrastructure. You can change all of the following in place:

  * The edition that your Cloud SQL instance uses.
  * The machine type.
  * The storage type.
  * The database version.



Making in-place changes is the most direct and least error-prone way to reconfigure an instance.

For more information about in-place upgrades and downgrades, see [Upgrade in place](https://docs.cloud.google.com/sql/docs/mysql/upgrade-in-place).

## September 02, 2026

Feature

Cloud SQL supports Workforce Identity Federation authentication. This lets you authenticate to your Cloud SQL instance using identities from an external identity provider such as Microsoft Active Directory or Okta. For more information, see [Workforce Identity Federation authentication](https://docs.cloud.google.com/sql/docs/mysql/workforce-authentication).

## August 27, 2026

Feature

Cloud SQL now makes it easier to configure [Private Service Connect](https://docs.cloud.google.com/sql/docs/mysql/about-private-service-connect) for your Cloud SQL instance. When you create an instance that's enabled with Private Service Connect, you can choose to automatically create the service connection policy and endpoint in the VPC network that you want to use with Private Service Connect.

For more information, see [Configure Private Service Connect](https://docs.cloud.google.com/sql/docs/mysql/configure-private-service-connect).

## August 13, 2026

Feature

[Cloud SQL for MySQL 9.7](https://docs.cloud.google.com/sql/docs/mysql/db-versions) is generally available ([GA](https://cloud.google.com/products#product-launch-stages)).

For more information about the differences between MySQL 9.7 and previous versions, review the [MySQL 9.7 Release Notes](https://dev.mysql.com/doc/relnotes/mysql/9.7/en/).

By default, if you specify MySQL 9.7 as the version when you create a Cloud SQL instance (either primary or replica) using the gcloud CLI, the Google Cloud console, or the REST API, then the Cloud SQL edition is Cloud SQL Enterprise Plus edition.

This release introduces support for key MySQL 9.7 capabilities, including:

  * [**Vector search**](https://docs.cloud.google.com/sql/docs/mysql/vector-search#version-differences): support for the community-standard vector storage format combined with advanced approximate nearest neighbor (ANN) vector indexing in Cloud SQL.
  * [**Hypergraph optimizer**](https://blogs.oracle.com/mysql/the-hypergraph-optimizer-is-now-available-in-mysql-9-7-community-edition): an alternative join-planning framework designed for complex, multi-table queries. You can enable the hypergraph optimizer using an [optimizer switch](https://dev.mysql.com/doc/refman/9.7/en/switchable-optimizations.html).
  * [**JSON Duality Views**](https://dev.mysql.com/doc/refman/9.7/en/json-duality-views.html): a feature that bridges relational SQL and hierarchical JSON document models to interact with the same underlying data.
  * **Upgrade and migration paths** : support for [in-place major version upgrade](https://docs.cloud.google.com/sql/docs/mysql/upgrade-major-db-version-inplace) from Cloud SQL for MySQL 8.4 and [migrations from MySQL 8.4 using the Database Migration Service (DMS)](https://docs.cloud.google.com/database-migration/docs/mysql/migration-src-and-dest#cross-version-support).

**Note:** The legacy `mysql_native_password` authentication plugin is no longer supported starting in Cloud SQL for MySQL 9.7. You must update all clients that use built-in authentication user accounts to use the `caching_sha2_password` plugin instead. For more information, see [MySQL authentication](https://docs.cloud.google.com/sql/docs/mysql/features#mysql-authentication).

### Flag updates for MySQL 9.7

Additionally, this release introduces several database flag changes.

MySQL database flag | Action | Details  
---|---|---  
`activate_mandatory_roles` | Added / Supported | Exposes mandatory roles configuration. Default is ON.  
`innodb_native_foreign_keys` | Added / Supported | Exposes SQL layer foreign key handling configuration.  
`table_open_cache_triggers` | Added / Supported | Configures trigger cache size limits.  
`connection_memory_status_limit` | Added / Supported | Sets limit configurations on connection memory.  
`global_connection_memory_status_limit` | Added / Supported | Sets global limit configurations on connection memory.  
`performance_schema_max_logger_classes` | Added / Supported | Sets limits for performance schema logger classes.  
`caching_sha2_password_proxy_users` | Added / Supported | Configures proxy users support for caching SHA-2.  
`caching_sha2_password_enforce_storage_format` | Added / Supported | Enforces storage format rules for caching SHA-2.  
`caching_sha2_password_storage_format` | Added / Supported | Sets storage format defaults for caching SHA-2.  
`innodb_log_file_size` | Removed | Flag not supported in MySQL 9.7 and later.  
`innodb_log_files_in_group` | Removed | Flag not supported in MySQL 9.7 and later.  
`innodb_undo_tablespaces` | Removed | Flag not supported in MySQL 9.7 and later.  
`mysql_native_password_proxy_users` | Removed | Flag not supported in MySQL 9.7 and later.  
`replica_parallel_type` | Removed | Flag not supported in MySQL 9.7 and later.  
`slave_parallel_type` | Removed | Flag not supported in MySQL 9.7 and later.  
`temptable_use_mmap` | Removed | Flag not supported in MySQL 9.7 and later.  
  
For more information about MySQL database flags, see [Configure database flags](https://docs.cloud.google.com/sql/docs/mysql/flags).

## August 11, 2026

Feature

The Cloud SQL remote MCP server now supports specialized endpoint URLs (toolsets) for `/readonly`, `/instance_manage`, and `/query_execution`. Specialized toolset URLs let you restrict the set of exposed MCP tools based on your security and workflow requirements.

For more information, see [Available toolsets](https://docs.cloud.google.com/sql/docs/mysql/use-cloudsql-mcp#available-toolsets).

Feature

You can now use the `create_instance` tool in the Cloud SQL remote MCP server to provision free trial instances for testing and development by setting the `free_trial` parameter to `true`.

For more information, see [Create a free trial instance](https://docs.cloud.google.com/sql/docs/mysql/use-cloudsql-mcp#create-free-trial).

Feature

When executing SQL queries using the `execute_sql` or `execute_sql_readonly` tool, setting the `sql_commenter_enabled` parameter to `true` automatically appends sqlcommenter tags (`mcp.tool`, `mcp.server`, `user.identity`, `mcp.client`) to SQL statements for enhanced database observability.

For more information, see [sqlcommenter tags](https://docs.cloud.google.com/sql/docs/mysql/use-cloudsql-mcp#sqlcommenter).

## August 07, 2026

Change

Newly created instances configured with [high availability (HA)](https://docs.cloud.google.com/sql/docs/mysql/high-availability) now have [Knowledge Catalog (formerly Dataplex Universal Catalog)](https://docs.cloud.google.com/sql/docs/mysql/dataplex-catalog-integration) enabled by default.

Cloud SQL for MySQL instances running on MySQL version 8.0 or later send updates and metadata to Knowledge Catalog in near real-time.

You can either verify enablement or [disable the feature](https://docs.cloud.google.com/sql/docs/mysql/dataplex-catalog-integration#deactivate-dataplex-catalog) using the Google Cloud console.

For more information, see [Near real-time](https://docs.cloud.google.com/sql/docs/mysql/dataplex-catalog-integration#near-real-time).

## August 05, 2026

Feature

Performance capture for Cloud SQL for MySQL is now generally available ([GA](https://cloud.google.com/products#product-launch-stages)). Performance capture lets you take a point-in-time snapshot of your database and operating system metrics automatically and route them to Cloud Logging for root-cause analysis.

With the GA release, you can configure custom thresholds that [end long-running transactions automatically](https://docs.cloud.google.com/sql/docs/mysql/configure-performance-capture#end-transactions) before they slow down your database. In addition, the GA release includes six additional performance capture triggers:

  * High CPU utilization
  * High memory usage
  * High temporary files usage
  * History list length
  * Semaphore waits
  * Transaction lock waits



For more information, see [Cloud SQL performance capture overview](https://docs.cloud.google.com/sql/docs/mysql/performance-capture).

## August 04, 2026

Feature

[DNS automation](https://docs.cloud.google.com/sql/docs/mysql/configure-dns#dns-auto) is now generally available ([GA](https://cloud.google.com/products#product-launch-stages)) on Cloud SQL instances where Private Service Connect is enabled.

You can use DNS automation to provision and manage per-instance DNS records automatically. On Enterprise Plus edition instances where DNS automation is enabled, you can also enable a global write endpoint DNS that automatically resolves to your current primary instance.

Feature

Cloud SQL for MySQL supports [resource groups](https://dev.mysql.com/doc/refman/8.0/en/resource-groups.html). MySQL resource groups let you manage resource allocation for different workloads on your Cloud SQL for MySQL instance. By using resource groups, you can prevent less important workloads from consuming excessive CPU or memory resources.

To use MySQL resource groups, you must have maintenance version [_MYSQL_VERSION_.R20260320.00_20](https://docs.cloud.google.com/sql/docs/mysql/maintenance-changelog) or later installed on your instance.

For more information, see [Manage CPU allocation with MySQL resource groups](https://docs.cloud.google.com/sql/docs/mysql/resource-groups).

## August 03, 2026

Change

You can change the backup plan for your [Cloud SQL enhanced backups](https://docs.cloud.google.com/sql/docs/mysql/backup-recovery/manage-enhanced-backups) without first removing the existing plan. For more information, see [Change your instance's associated backup plan](https://docs.cloud.google.com/sql/docs/mysql/backup-recovery/manage-enhanced-backups#change-plan).

## July 31, 2026

Change

Starting on August 1, 2026, when you create or clone a Cloud SQL instance enabled with Private Service Connect, or when you enable Private Service Connect for an existing instance, then [connection reconciliation](https://docs.cloud.google.com/vpc/docs/about-controlling-access-published-services#connection-reconciliation) behavior is enabled by default and can't be disabled.

When you remove a project from the list of allowed projects, all existing Private Service Connect connections from the removed project are immediately closed (reconciled). This means that applications using Private Service Connect endpoints in those removed projects can't continue to connect to the Cloud SQL instance using those endpoints.

For more information, see [Allowed Private Service Connect projects](https://docs.cloud.google.com/sql/docs/mysql/about-private-service-connect#allowed-psc-projects).

Feature

QueryData adds support for parameterized secure views (PSVs) to help secure applications that use natural language queries. For more information, see [Secure and control access to application data](https://docs.cloud.google.com/gemini/data-agents/querydata/sql-mysql/secure-app-data-parameterized-secure-views-qd).

This feature is in [Preview](https://cloud.google.com/products#product-launch-stages).

## July 29, 2026

Feature

Cloud SQL for MySQL now supports significantly faster re-encryption of instances and replicas protected by customer-managed encryption keys (CMEKs), and re-encryption now completes with zero downtime. The steps to re-encrypt your instances and replicas are unchanged, but the operation now re-encrypts the underlying disks in-place, without creating re-encryption backups.

For more information, see [Re-encrypt an existing CMEK-enabled instance or replica](https://docs.cloud.google.com/sql/docs/mysql/configure-cmek#reencrypt).

## July 16, 2026

Change

Cloud SQL for MySQL 8.4.8 is upgraded to MySQL 8.4.10. For more information, see the [MySQL 8.4.10 Release Notes](https://dev.mysql.com/doc/relnotes/mysql/8.4/en/news-8-4-10.html) and [Cloud SQL database versions](https://docs.cloud.google.com/sql/docs/mysql/db-versions).

## July 13, 2026

Feature

You can now create and query parameterized secure views in Cloud SQL for MySQL. Parameterized secure views let you create MySQL views in your MySQL database that reference session variables for managing data access. By using a parameterized secure view, you can create a single view that is flexible enough to accommodate multiple queries across a predefined range of data without being required to create multiple static view definitions for different users.

To use parameterized secure views, you're required to have Cloud SQL for MySQL 8.0.43 or later and [maintenance version R20260320.00_20 or later](https://docs.cloud.google.com/sql/docs/mysql/maintenance-changelog) installed on your instance.

For more information, see [Parameterized secure views in Cloud SQL](https://docs.cloud.google.com/sql/docs/mysql/parameterized-secure-views). This feature is in [Preview](https://cloud.google.com/products#product-launch-stages).

## June 29, 2026

Feature

MySQL 8.0.45 is now the [default minor version](https://docs.cloud.google.com/sql/docs/mysql/db-versions#database-version-support) for Cloud SQL for MySQL 8.0.

For more information about minor version support in Cloud SQL for MySQL, see [MySQL 8.0](https://docs.cloud.google.com/sql/docs/mysql/db-versions#mysql-8.0).

## June 25, 2026

Feature

You can now assess the upgrade readiness of your Cloud SQL for MySQL instances before a major version upgrade by running a precheck. This precheck analyzes your instance for version incompatibilities and lists any issues that need to be fixed prior to your upgrade. For more information, see [Assess upgrade readiness for your instance](https://docs.cloud.google.com/sql/docs/mysql/upgrade-major-db-version-inplace#precheck).

This feature is in [Preview](https://cloud.google.com/products#product-launch-stages).

## June 24, 2026

Change

Cloud SQL now supports Private Service Connect outbound connectivity on the following additional types of instances:

  * Read replica instances.

  * Instances that use advanced disaster recovery features such as switchover and failover operations.




For more information about Private Service Connect outbound connectivity see [About Private Service Connect](https://docs.cloud.google.com/sql/docs/mysql/about-private-service-connect#psc-outbound).

## June 19, 2026

Change

When you [migrate from Percona XtraBackup physical file to Cloud SQL for MySQL](https://docs.cloud.google.com/sql/docs/mysql/migrate-xtrabackup-physical-file), you can now specify multiple data files in the `innodb_data_file_path` parameter of your external server configuration. Also, you are no longer required to use the default name for your data files.

Change

Cloud SQL for MySQL now supports multiple system tablespace files, allowing [system tablespace size](https://docs.cloud.google.com/sql/docs/quotas#table_limit) to grow larger than 16TB.

## June 18, 2026

Feature

Cloud SQL for MySQL now supports minor version [8.0.46](https://dev.mysql.com/doc/relnotes/mysql/8.0/en/news-8-0-46.html). To upgrade your existing instance to the new minor version, see [Upgrade the database minor version](https://docs.cloud.google.com/sql/docs/mysql/upgrade-minor-db-version#manual-upgrade).

## June 15, 2026

Feature

You can publish a [Cloud SQL for MySQL conversational analytics agent in Gemini Enterprise](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics/sql-mysql/create-data-agents#publish-agent-gemini-enterprise). This feature is in [Preview](https://cloud.google.com/products#product-launch-stages).

## June 08, 2026

Feature

Cloud SQL for MySQL [managed buffer pool](https://docs.cloud.google.com/sql/docs/mysql/optimize-high-memory-usage#enable-managed-buffer-pool) is now generally available ([GA](https://cloud.google.com/products#product-launch-stages)). Managed buffer pool helps you avoid out-of-memory events (OOMs) on your Cloud SQL instance by reducing `innodb_buffer_pool_size` when memory usage is high.

Change

Cloud SQL Enterprise Plus arm-based C4A machine types, powered by Google's Axion processors, are now available in 8 additional regions:

  * `asia-northeast1`: Tokyo, Japan
  * `australia-southeast2`: Melbourne, Australia
  * `europe-north1`: Finland
  * `northamerica-northeast1`: Montréal, Québec, Canada
  * `northamerica-northeast2`: Toronto, Ontario, Canada
  * `southamerica-west1`: Santiago, Chile
  * `us-east5`: Columbus, Ohio, USA
  * `us-west2`: Los Angeles, California, USA



For information about C4A machine types, see [The C4A machine series](https://docs.cloud.google.com/sql/docs/mysql/machine-series-overview#c4a).

## May 12, 2026

Change

The command for upgrading Cloud SQL instances to the new network architecture has been re-enabled.

For more information, see [Upgrade an instance to the new network architecture](https://docs.cloud.google.com/sql/docs/mysql/upgrade-cloud-sql-instance-new-network-architecture) .

## May 11, 2026

Feature

Cloud SQL for MySQL now supports regional endpoints for the Cloud SQL Admin API. This feature lets you direct your API calls to a region-specific endpoint. Using a regional endpoint enhances data locality and helps meet strict compliance expectations.

This feature includes: * **Regional boundary restrictions** : Cloud SQL regional endpoints enforce strict matching. The region of the target API resource must match the region of the endpoint exactly. Otherwise, the request is rejected with a 4xx error. * **Restricted API visibility** : When you use a regional endpoint, the Instance.List API only returns resources located within that specific region.

For more information, see [Cloud SQL regional endpoints](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rep).

This feature is in [Preview](https://cloud.google.com/products#product-launch-stages).

## April 30, 2026

Fixed

Cloud SQL has made the following enhancements to expand the list of eligible Cloud SQL Enterprise Plus edition instances that support planned operations with [near-zero downtime](https://docs.cloud.google.com/sql/docs/mysql/availability#near-zero-downtime).

  * Instances with [connector enforcement enabled](https://docs.cloud.google.com/sql/docs/mysql/connect-connectors#enforce) are eligible for planned operations with near-zero downtime.
  * Instances that use [private services access](https://docs.cloud.google.com/sql/docs/mysql/configure-private-services-access) with a non-RFC 1918 IP address are eligible for planned operations with near-zero downtime.



## April 20, 2026

Feature

You can use the [Database Insights remote MCP server](https://docs.cloud.google.com/sql/docs/mysql/reference/mcp/databaseinsights/mcp) to analyze Cloud SQL for MySQL's performance and system metrics. This feature is in [GA](https://cloud.google.com/products#product-launch-stages).

## April 18, 2026

Feature

Newly created Cloud SQL instances are integrating with Knowledge Catalog (formerly Dataplex Universal Catalog) for data discovery. Instances on MySQL version 8.0 or later will have updates sent to Knowledge Catalog in near real-time. As part of this automatic enablement, we will send metadata to Knowledge Catalog. You can verify if your instance is enabled for integration with Knowledge Catalog by looking at the configuration pane in the Knowledge Catalog console. If you don't want your instance to be integrated with Knowledge Catalog, you can [turn off this feature](https://docs.cloud.google.com/sql/docs/mysql/dataplex-catalog-integration#deactivate-dataplex-catalog).

For more information, see [Near real-time](https://docs.cloud.google.com/sql/docs/mysql/dataplex-catalog-integration#near-real-time).

## April 16, 2026

Feature

The [Cloud SQL remote MCP server](https://docs.cloud.google.com/sql/docs/mysql/use-cloudsql-mcp) is generally available ([GA](https://cloud.google.com/products#product-launch-stages)). The Cloud SQL remote MCP server lets you interact easily with Cloud SQL instances from LLMs, AI applications, and AI-enabled development platforms.

Feature

You can use [DNS automation](https://docs.cloud.google.com/sql/docs/mysql/about-private-service-connect#dns-automation) on Cloud SQL instances where Private Service Connect is enabled to provision and manage per-instance DNS records automatically. On Enterprise Plus edition instances where DNS automation is enabled, you can also enable a global write endpoint DNS that automatically resolves to your current primary instance.

This feature is in [Preview](https://cloud.google.com/products#product-launch-stages).

## April 14, 2026

Breaking

As of April 10, 2026, you can create, run, and edit [Gemini Cloud Assist investigations](https://docs.cloud.google.com/cloud-assist/investigations) only if you have a [Premium Support contract](https://cloud.google.com/support/premium). You can use Gemini Cloud Assist investigations to [monitor and troubleshoot your Cloud SQL instance with AI assistance](https://docs.cloud.google.com/sql/docs/mysql/monitor-troubleshoot-with-ai).

If you ran an investigation prior to April 10, 2026, then the results of the investigation continue to be available to you in the Google Cloud console.

## April 06, 2026

Feature

If the storage capacity of a Cloud SQL instance is larger than your application needs, then you can manually reduce, or shrink, your storage capacity to a smaller size.

Depending on underlying disk size, storage shrink operations might incur considerable downtime. If your instance requires limited downtime, rather than using storage shrink capabilities, we recommend migrating your data to a new, smaller instance using Database Migration Service.

For more information, see [About storage shrink](https://docs.cloud.google.com/sql/docs/mysql/about-storage-shrink).

Feature

The QueryData tool lets you to query the data in your database using conversational language and build data agents. For more information, see [QueryData tool overview](https://docs.cloud.google.com/gemini/data-agents/querydata/sql-mysql/data-agent-overview). This feature is available in ([Preview](https://cloud.google.com/products#product-launch-stages)).

The preview release increases the accuracy of SQL generation with value search queries which match values and their context within a database. Value search queries trigger automatically.

## March 31, 2026

Feature

You can now migrate a subset of databases from an external server to a destination Cloud SQL for MySQL instance.

For more information, see [Configure Cloud SQL and the external server for replication](https://docs.cloud.google.com/sql/docs/mysql/replication/configure-replication-from-external).

## March 30, 2026

Feature

Cloud SQL for MySQL now offers conversational analytics, which lets users query their operational data using natural language. This feature is powered by the [Conversational Analytics API](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/overview), which can help you translate complex human dialog into precise database queries to provide actionable insights. This feature is in [Preview](https://cloud.google.com/products#product-launch-stages). For more information, see [Conversational analytics for Cloud SQL for MySQL overview](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics/sql-mysql).

## March 26, 2026

Feature

MySQL 8.0.44 is now the [default minor version](https://docs.cloud.google.com/sql/docs/mysql/db-versions#database-version-support) for Cloud SQL for MySQL 8.0.

For more information about minor version support in Cloud SQL for MySQL, see [MySQL 8.0](https://docs.cloud.google.com/sql/docs/mysql/db-versions#mysql-8.0).

## March 20, 2026

Feature

Cloud SQL for MySQL now supports minor version [8.0.45](https://dev.mysql.com/doc/relnotes/mysql/8.0/en/news-8-0-45.html). To upgrade your existing instance to the new minor version, see [Upgrade the database minor version](https://docs.cloud.google.com/sql/docs/mysql/upgrade-minor-db-version#manual-upgrade).

## March 17, 2026

Feature

[Multi-region backup vaults for Cloud SQL enhanced backups](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-vault#multi-regions) are generally available (GA).

This feature lets you store your backup data in multi-region storage locations, providing higher availability and protection against regional outages.

For more information, see [Enhanced backups](https://docs.cloud.google.com/sql/docs/mysql/backup-recovery/backup-options#enhanced-backups) .

Feature

Cloud SQL supports cross-project PITR operations for instances protected by backup and DR ([GA](https://cloud.google.com/products#product-launch-stages)).

This feature lets you restore a Cloud SQL instance to a project other than the project where either the source instance or the backup vault is located.

For more information, see [Perform a cross-project PITR](https://docs.cloud.google.com/sql/docs/mysql/backup-recovery/pitr#perform_a_cross-project_pitr) .

## March 13, 2026

Feature

You can now enable automatic server certificate rotation for your Cloud SQL instance. This feature is specifically designed for instances utilizing the Certificate Authority Service (CAS). Automatic server certificate rotation helps you maintain high security standards while removing the operational burden of manual rotation.

For more information about enabling automatic server certificate rotation for your instance, see [Enable automatic server certificate rotation](https://docs.cloud.google.com/sql/docs/mysql/manage-ssl-instance#automatic-server-certificate-rotation-cas) .

## March 09, 2026

Feature

You can now execute SQL statements using the [Cloud SQL Data API](https://docs.cloud.google.com/sql/docs/mysql/executesql-instance) for administrative queries.

## March 02, 2026

Feature

Cloud SQL for MySQL 8.4.7 is upgraded to MySQL 8.4.8. For more information, see the [MySQL 8.4.8 Release Notes](https://dev.mysql.com/doc/relnotes/mysql/8.4/en/news-8-4-8.html).

## February 24, 2026

Feature

It now takes less time to create a Cloud SQL instance when point-in-time recovery (PITR) is enabled, as it is by default in the Google Cloud console. During instance creation, PITR now initially uses an [instant snapshot](https://docs.cloud.google.com/compute/docs/disks/instant-snapshots) instead of a [standard backup](https://docs.cloud.google.com/sql/docs/mysql/backup-recovery/backups#backup-options). and then later converts the snapshot to a standard backup in the background to support [restore operations](https://docs.cloud.google.com/sql/docs/mysql/backup-recovery/restore#tips-pitr).

## February 23, 2026

Feature

Gemini Cloud Assist investigation capabilities are now supported in Cloud SQL for MySQL ([Preview](https://cloud.google.com/products#product-launch-stages)).

For more information, see [Troubleshoot slow queries with AI assistance](https://docs.cloud.google.com/sql/docs/mysql/monitor-troubleshoot-with-ai#troubleshoot-slow-queries).

## February 18, 2026

Deprecated

Control of MCP use with organization policies is deprecated. After March 17, 2026, organization policies that use the `gcp.managed.allowedMCPServices` constraint won't work, and you can control MCP use with IAM deny policies. For more information about controlling MCP use, see [Control MCP use with IAM](https://docs.cloud.google.com/mcp/control-mcp-use-iam).

Change

After March 17, 2026, when you enable the Cloud SQL Admin API (`sqladmin.googleapis.com`), the Cloud SQL remote MCP server is enabled automatically.

The Cloud SQL remote MCP server is in [Preview](https://cloud.google.com/products#product-launch-stages).

## February 17, 2026

Announcement

New best practices are available for securing generative AI agents using Model Context Protocol (MCP) with Google Cloud databases. This guide covers key security measures like least privilege, native database controls, and secure agent design to help you build safer AI applications. For more information, see [Best practices for securing agent interactions with Model Context Protocol](https://docs.cloud.google.com/sql/docs/mysql/secure-agent-interactions-mcp) .

## February 10, 2026

Feature

[Model endpoint management](https://docs.cloud.google.com/sql/docs/mysql/model-endpoint-overview) for Cloud SQL for MySQL and the [integration of Cloud SQL for MySQL with Vertex AI](https://docs.cloud.google.com/sql/docs/mysql/integrate-cloud-sql-with-vertex-ai) are now generally available ([GA](https://cloud.google.com/products#product-launch-stages)).

By integrating your Cloud SQL for MySQL instance with Vertex AI, you can invoke online predictions and generate vector embeddings from models hosted in Vertex AI directly from your Cloud SQL instance.

With model endpoint management, you can build generative AI applications by integrating your databases with models from third-party providers like OpenAI using your own API keys. Model endpoint management lets you register and manage model endpoints for your MySQL instance, making your interactions with a wider range of ML models seamless.

## February 09, 2026

Feature

You can now use the [Cloud SQL remote MCP server](https://docs.cloud.google.com/sql/docs/mysql/use-cloudsql-mcp) . The Cloud SQL remote MCP server lets you interact easily with Cloud SQL instances from LLMs, AI applications, and AI-enabled development platforms.

This feature is in [Preview](https://cloud.google.com/products#product-launch-stages).

## February 02, 2026

Feature

You can now update the server certificate authority (CA) mode of an existing Cloud SQL instance. You can update existing instances that use the per-instance CA option (`GOOGLE_MANAGED_INTERNAL_CA`) to use the shared CA option (`GOOGLE_MANAGED_CAS_CA`) or the customer-managed CA option (`CUSTOMER_MANAGED_CAS_CA`).

For more information about the different server CA mode options, see [Certificate authority (CA) hierarchies](https://docs.cloud.google.com/sql/docs/mysql/authorize-ssl#ca-hierarchies).

## January 26, 2026

Feature

You can now assign database roles to built-in database users and IAM database users when you create or update users. For more information about assigning roles, see [built-in database authentication](https://docs.cloud.google.com/sql/docs/mysql/create-manage-users#creating) or [IAM database authentication](https://docs.cloud.google.com/sql/docs/mysql/add-manage-iam-users#add-db-roles) .

## January 23, 2026

Feature

Cloud SQL for MySQL now supports performance capture to help you diagnose transient performance issues with your MySQL database. Performance capture lets you specify configurable thresholds for additional monitoring. If a threshold is reached, then performance capture takes snapshots of the database state, including in-flight transactions, InnoDB status, and, in the case of replication lag, detailed replication status. Performance capture outputs the snapshots in a log format so you can review the state of the instance when the problem occurred.

For more information, see [Cloud SQL performance capture overview](https://docs.cloud.google.com/sql/docs/mysql/performance-capture) . Performance capture is in [Preview](https://cloud.google.com/products#product-launch-stages).

## January 21, 2026

Change

Cloud SQL for MySQL 8.0.43 is now the [default minor version](https://docs.cloud.google.com/sql/docs/mysql/db-versions#database-version-support) of Cloud SQL for MySQL 8.0.

If you have automatic minor version upgrade enabled for your instance, then your instance is upgraded to the default minor version automatically during its regularly scheduled maintenance update.

For more information about automatic minor version upgrade, see [Upgrade the database minor version of MySQL 8.0](https://docs.cloud.google.com/sql/docs/mysql/upgrade-minor-db-version).

## January 15, 2026

Feature

Cloud SQL for MySQL now supports fast clone operations within the same zone ([GA](https://cloud.google.com/products#product-launch-stages)).

For more information, see [Clone an instance](https://docs.cloud.google.com/sql/docs/mysql/clone-instance).

## December 17, 2025

Feature

You can build data agents that interact with the data in your database using conversational language. Use these data agents as tools to empower your applications. For more information, see [Data agents overview](https://docs.cloud.google.com/sql/docs/mysql/data-agent-overview). This feature is available in [Preview](https://cloud.google.com/products#product-launch-stages), and access to it requires a [sign-up](https://forms.gle/pJByTWfenZAWbaXo7).

## December 16, 2025

Feature

Cloud SQL enhanced backups are now generally available ([GA](https://cloud.google.com/products#product-launch-stages)).

With enhanced backups, backups are managed and stored in a centralized backup management project that leverages the [Backup and DR service](https://docs.cloud.google.com/backup-disaster-recovery/docs), and provides enforced retention, granular scheduling, and longer retention.

Enhanced backups now also support [point-in-time-recovery (PITR) after instance deletion](https://docs.cloud.google.com/sql/docs/mysql/backup-recovery/restore).

For more information about the available options and their limitations, see [Backup options](https://docs.cloud.google.com/sql/docs/mysql/backup-recovery/backup-options). For more information about enhanced backups pricing, see [Backup and DR pricing](https://cloud.google.com/backup-disaster-recovery/pricing).

## November 21, 2025

Feature

To help prevent out-of-memory (OOM) events, you can enable managed buffer pool for Cloud SQL for MySQL 8.0 and later instances. When you enable managed buffer pool, Cloud SQL reduces the value of the `innodb_buffer_pool_size` configuration and frees up memory when memory usage is high, and the instance is in danger of an OOM event. After memory usage stabilizes at a lower value, MySQL increases the value of `innodb_buffer_pool_size` incrementally to its original value.

To enable managed buffer pool, your Cloud SQL instance must use a maintenance version of [ ` [$MYSQL_VERSION].R20251004.01_07 ` ](https://docs.cloud.google.com/sql/docs/mysql/maintenance-changelog) or later. You can't enable managed buffer pool for instances that use a shared core or for instances that are running MySQL 5.6 or MySQL 5.7.

For more information, see [Enable managed buffer pool](https://docs.cloud.google.com/sql/docs/mysql/optimize-high-memory-usage#enable-managed-buffer-pool) . Support for managed buffer pool is in [Preview](https://cloud.google.com/products#product-launch-stages).

## November 18, 2025

Feature

Cloud SQL for MySQL 8.4.6 is upgraded to MySQL 8.4.7. For more information, see the [MySQL 8.4.7 Release Notes](https://dev.mysql.com/doc/relnotes/mysql/8.4/en/news-8-4-7.html).

## November 17, 2025

Feature

Cloud SQL now offers a free trial instance for both existing and new Google Cloud customers. A free trial instance lets you test advanced Cloud SQL capabilities and features for up to 30 days without any financial commitment.

For information about a free trial instance, and its inclusions and conditions, see [Free trial instance overview](https://docs.cloud.google.com/sql/docs/mysql/free-trial-instance).

## November 14, 2025

Feature

Cloud SQL for MySQL now supports [read pool autoscaling](https://docs.cloud.google.com/sql/docs/mysql/read-pool-autoscaling) [(GA)](https://cloud.google.com/products#product-launch-stages), which helps you more easily manage your application's workload needs.

This feature automates read pool scale in and scale out operations based on one or both of the following conditions:

  * Allowed CPU usage of the read pool
  * Allowed number of client connections to the read pool



## November 13, 2025

Feature

Cloud SQL for MySQL now lets you have more control over the number of results that are returned when you perform an ANN vector search with filters. You can use iterative filtering when the selective filters of the `WHERE` clause in your ANN search query produce fewer results than the number of results specified in your `LIMIT` clause.

To enable iterative filtering for your ANN search query, set the `cloudsql_vector_iterative_filtering` flag to `ON`. You can set the flag at a session or global level.

To enable and use iterative filtering for your ANN search query, you must have [`[MYSQL_$VERSION].R20251004.01_07`](https://docs.cloud.google.com/sql/docs/mysql/maintenance-changelog) or later installed on your MySQL instance.

For more information, see [Search approximate nearest neighbors (ANN)](https://docs.cloud.google.com/sql/docs/mysql/search-filter-vector-embeddings#ann) .

## November 12, 2025

Feature

Cloud SQL for MySQL now supports minor version [8.0.44](https://dev.mysql.com/doc/relnotes/mysql/8.0/en/news-8-0-44.html). To upgrade your existing instance to the new version, see [Upgrade the database minor version](https://docs.cloud.google.com/sql/docs/mysql/upgrade-minor-db-version#manual-upgrade).

## November 10, 2025

Feature

Cloud SQL now provides brute-force detection and protection for your Cloud SQL instances. This helps protect your instances from brute-force access attempts by identifying the source and mitigating the risk caused by these attempts. For more information, see [Use brute-force protection](https://docs.cloud.google.com/sql/docs/mysql/use-brute-force-protection).

## November 04, 2025

Feature

Cloud SQL now supports the [automatic minor version upgrade](https://docs.cloud.google.com/sql/docs/mysql/upgrade-minor-db-version#auto-upgrade) for Cloud SQL for MySQL 8.0.35 or later instances. If your Cloud SQL for MySQL instance is running MySQL 8.0.35 or later, but you didn't select a specific minor version when you created the instance (`databaseVersion=MYSQL_8_0`), then your MySQL instance is upgraded automatically to the [**default minor version**](https://docs.cloud.google.com/sql/docs/db-versions#database-version-support) of Cloud SQL for MySQL 8.0 during its [regular scheduled maintenance update](https://docs.cloud.google.com/sql/docs/mysql/maintenance) .

All eligible Cloud SQL for MySQL instances receive the first automatic minor version upgrade during the rollout of [ ` MYSQL_8_0_[ _N_ ].R20251004.01_07 ` ](https://docs.cloud.google.com/sql/docs/mysql/maintenance-changelog/mysql-8-0#mysql_8_0_%5B18,-26,-27,-28,-30,-31,-32,-33,-34,-35,-36,-37,-39,-40,-41,-42,-43%5D.r20251004.01_07).

## October 28, 2025

Feature

Cloud SQL has enhanced the optimized writes feature, which includes an improved crash recovery algorithm to reduce crash recovery time and utilizes unused disk I/O throughput adaptively to accelerate buffer pool warm-up. The optimized writes feature provides a set of write performance improvements that adjust MySQL configurations dynamically based on workload demand and underlying infrastructure.

By default these improvements are enabled for all new Cloud SQL Enterprise Plus edition instances that you create or that you upgrade to from Cloud SQL Enterprise edition.

For more information about optimized writes, see [Configure database flags](https://docs.cloud.google.com/sql/docs/mysql/flags#tips-optimized-write).

## October 17, 2025

Feature

Cloud SQL Enterprise edition now supports a new machine series called the N4 machine series. This machine series provides balanced price-to-performance and uses the Hyperdisk Balanced storage. You can create custom machine types for the N4 machine series with up to 80 vCPUs and up to 640 GB memory. The N4 machine series is [generally available](https://cloud.google.com/products#product-launch-stages) (GA).

For more information about the N4 machine series and its availability, see [Machine series overview](https://docs.cloud.google.com/sql/docs/mysql/machine-series-overview).

Feature

The [C4A machine series](https://docs.cloud.google.com/sql/docs/mysql/machine-series-overview#c4a) is now [generally available](https://cloud.google.com/products#product-launch-stages) (GA).

The C4A machine series is supported for Cloud SQL Enterprise Plus edition instances, and provides optimized price-performance and delivers predictable high performance for high demand Cloud SQL workloads. It uses the Hyperdisk Balanced storage.

For more information about the C4A machine series and its availability, see [Machine series overview](https://docs.cloud.google.com/sql/docs/mysql/machine-series-overview).

## September 29, 2025

Feature

You can now [use Gemini's capabilities to fix errors in a query within Cloud SQL Studio](https://docs.cloud.google.com/sql/docs/mysql/write-sql-gemini#fix-query) ([Preview](https://cloud.google.com/products#product-launch-stages)).

## September 25, 2025

Feature

Cloud SQL for MySQL now supports minor version 8.0.43. To upgrade your existing instance to the new version, see [Upgrade the database minor version](https://docs.cloud.google.com/sql/docs/mysql/upgrade-minor-db-version).

## September 24, 2025

Feature

Cloud SQL for MySQL 8.4.5 is upgraded to MySQL 8.4.6. For more information, see the [MySQL 8.4.6 Release Notes](https://dev.mysql.com/doc/relnotes/mysql/8.4/en/news-8-4-6.html).

## September 23, 2025

Feature

You can now provision, manage and query your databases using the dedicated Gemini CLI extension for Cloud SQL for MySQL. The extension provides full lifecycle control of your database—from provisioning instances, to exploring schemas and troubleshooting issues—from your command-line interface. 

For more information, see [Use Cloud SQL for MySQL with MCP, Gemini CLI, and other agents](https://docs.cloud.google.com/sql/docs/mysql/pre-built-tools-with-mcp-toolbox).

Feature

You can now retain point-in-time recovery (PITR) logs for an instance after its deletion for a specified retention period. These logs can be used to restore the deleted instance to a specific point in time. For more information, see [Restore a deleted instance using PITR](https://docs.cloud.google.com/sql/docs/mysql/backup-recovery/restore#deleted-instance).

## September 08, 2025

Feature

Cloud SQL read pools are now generally available and provide operational simplicity and scaling for your read workloads.

Read pools provide a single endpoint in front of up to 20 read pool nodes and automatically load balance traffic.

You can scale your read pool in several ways: 

  * **Scale in or out** : scale load balancing capacity horizontally by modifying the number of read pool nodes in the read pool. Each read pool supports up to 20 read pool nodes.
  * **Scale up or down** : scale load balancing capacity vertically by modifying the machine type associated with a read pool node. Once defined, configuration is uniformly applied across each read pool node in the read pool.



For more information, see [About read pools](https://docs.cloud.google.com/sql/docs/mysql/about-read-pools).

Feature

You can have Cloud SQL create a [Private Service Connect](https://docs.cloud.google.com/sql/docs/mysql/about-private-service-connect#psc-endpoint) endpoint automatically. You can use this endpoint to access Cloud SQL instances through a VPC network. For more information, see [Create a Private Service Connect endpoint automatically](https://docs.cloud.google.com/sql/docs/mysql/configure-private-service-connect#create-endpoint-automatically). 

This feature is now generally available ([GA](https://cloud.google.com/products#product-launch-stages)).

## September 04, 2025

Change

The release note on [August 13, 2025](https://docs.cloud.google.com/sql/docs/mysql/release-notes#August_13_2025) regarding Private Service Connect (PSC) outbound connectivity has been updated.

PSC outbound connectivity is required for [homogeneous migrations](https://docs.cloud.google.com/database-migration/docs/homogeneous-migrations) to PSC-enabled Cloud SQL instances using [Database Migration Service](https://docs.cloud.google.com/database-migration/docs). For more information, see [PSC outbound connections](https://docs.cloud.google.com/sql/docs/mysql/about-private-service-connect#psc-outbound).

## September 03, 2025

Feature

Cloud SQL Managed Connection Pooling is now generally available ([GA](https://cloud.google.com/products#product-launch-stages)). Managed Connection Pooling lets you scale your workloads by optimizing resource utilization for Cloud SQL instances using pooling. 

For more information, see [Managed Connection Pooling overview](https://docs.cloud.google.com/sql/docs/mysql/managed-connection-pooling).

Feature

You can now enable your instance to take a final backup at instance deletion and define its retention period by setting the final backup [instance setting](https://docs.cloud.google.com/sql/docs/mysql/instance-settings). 

You can also create a [custom organization policy](https://docs.cloud.google.com/sql/docs/mysql/org-policy/custom-org-policy) to define final backup instance settings. For more information, see [Final backup](https://docs.cloud.google.com/sql/docs/mysql/backup-recovery/backups#final-backup).

## August 21, 2025

Feature

You can save and manage SQL queries in Cloud SQL Studio. This feature is in [Preview](https://cloud.google.com/products#product-launch-stages). For more information, see [Saved queries overview](https://docs.cloud.google.com/sql/docs/mysql/saved-queries).

## August 15, 2025

Feature

Now you can use [Private Service Connect backends](https://docs.cloud.google.com/sql/docs/mysql/about-private-service-connect#psc-backend), as an alternative to Private Service Connect endpoints, to access Cloud SQL instances.

Feature

Now you can create an IPv6 endpoint for Private Service Connect (PSC) connections. For more information, see [Connect to an instance using Private Service Connect](https://docs.cloud.google.com/sql/docs/mysql/configure-private-service-connect#create-psc-endpoint).

Deprecated

You can no longer set a deny maintenance period for instances that are running a maintenance version older than 12 months. To update your instance, [perform self-service maintenance](https://docs.cloud.google.com/sql/docs/mysql/self-service-maintenance) or wait until the [next maintenance window](https://docs.cloud.google.com/sql/docs/mysql/set-maintenance-window#find-maintenance-api) to update your instance automatically. For more information about maintenance, see [Maintenance updates on Cloud SQL instances](https://docs.cloud.google.com/sql/docs/mysql/maintenance).

## August 13, 2025

Feature

Cloud SQL now supports Private Service Connect (PSC) outbound connectivity. With PSC outbound connectivity, you can attach a PSC interface to your existing Cloud SQL PSC-enabled instances to allow your instances to make outbound connections to your network. This is required for [homogeneous migrations](https://docs.cloud.google.com/database-migration/docs/homogeneous-migrations) to PSC-enabled Cloud SQL instances using [Database Migration Service](https://docs.cloud.google.com/database-migration/docs). For more information, see [PSC outbound connections](https://docs.cloud.google.com/sql/docs/mysql/about-private-service-connect#psc-outbound).

## August 07, 2025

Change

Cloud SQL for Enterprise Plus edition supports quality enhancements for [AI-assisted troubleshooting](https://docs.cloud.google.com/sql/docs/mysql/monitor-troubleshoot-with-ai). With AI-assisted troubleshooting, you can resolve complex database performance issues like [slow queries](https://docs.cloud.google.com/sql/docs/mysql/monitor-troubleshoot-with-ai#troubleshoot-slow-queries) and [high load](https://docs.cloud.google.com/sql/docs/mysql/monitor-troubleshoot-with-ai#troubleshoot-high-database-load) for your instances in a guided manner. To use AI-assisted troubleshooting, you need [Gemini Cloud Assist](https://docs.cloud.google.com/cloud-assist/overview) and [query insights](https://docs.cloud.google.com/sql/docs/mysql/using-query-insights#enable-insights) for Enterprise Plus edition.

## August 04, 2025

Feature

Cloud SQL for MySQL now supports [model endpoint management](https://docs.cloud.google.com/sql/docs/mysql/model-endpoint-overview) to help you build your generative AI applications. With model endpoint management, you can register and call remote AI model providers or access the Vertex AI integration. This feature is in [Preview](https://cloud.google.com/products#product-launch-stages) and available in Cloud SQL for MySQL version 8.0.36 and later, which includes Cloud SQL for MySQL version 8.4.

To use model endpoint management, update your instance to [`[_MySQL version_].R20250531.01_14`](https://docs.cloud.google.com/sql/docs/mysql/maintenance-changelog) or later, and make sure that you've enabled the [integration with Vertex AI](https://docs.cloud.google.com/sql/docs/mysql/integrate-cloud-sql-with-vertex-ai) on your instance. You can [perform self-service maintenance](https://docs.cloud.google.com/sql/docs/mysql/self-service-maintenance) or wait until the [next maintenance window](https://docs.cloud.google.com/sql/docs/mysql/set-maintenance-window#find-maintenance-api) to update the maintenance version of your instance automatically.

## July 31, 2025

Feature

Cloud SQL now offers two options of backup services to manage your instance's backups:

  * **Enhanced backups** ([Preview](https://cloud.google.com/products#product-launch-stages)): backups are managed and stored in a centralized backup management project that leverages the [Backup and DR service](https://docs.cloud.google.com/backup-disaster-recovery), and provides enforced retention, granular scheduling, and longer retention.

  * **Standard backups** (existing option): backups are created, managed, and stored in the same project as your Cloud SQL instances. 




You can choose between these options based on your instance's requirements and needs. Although instances can't use both backup options at the same time, Cloud SQL gives you the ability to switch between these backup options as necessary. 

For more information about the available options and their limitations, see [Backup options](https://docs.cloud.google.com/sql/docs/mysql/backup-recovery/backups#backup-options).

## July 02, 2025

Feature

The write endpoint feature for Cloud SQL Enterprise Plus edition instances is now [generally available](https://cloud.google.com/products#product-launch-stages) (GA). This endpoint is a global domain name service (DNS) name and resolves to the IP address of the current primary Cloud SQL instance that's enabled with private services access.

By using a write endpoint, you can avoid having to make application connection changes after performing a switchover or replica failover operation to test or mitigate a region failure.

For more information, see [Connect to an instance using a write endpoint](https://docs.cloud.google.com/sql/docs/mysql/connect-to-instance-using-write-endpoint).

## June 24, 2025

Feature

Cloud SQL for MySQL 8.4.4 is upgraded to MySQL 8.4.5. For more information, see the [MySQL 8.4.5 Release Notes](https://dev.mysql.com/doc/relnotes/mysql/8.4/en/news-8-4-5.html).

## June 17, 2025

Change

You no longer have to upgrade your instance to MySQL 8.0.37 before you upgrade to Cloud SQL for MySQL 8.4. You can upgrade to Cloud SQL for MySQL 8.4 from any minor version of Cloud SQL for MySQL 8.0. For more information about upgrading the major version of a Cloud SQL instance, see [Upgrade the database major version-place](https://docs.cloud.google.com/sql/docs/mysql/upgrade-major-db-version-inplace).

## May 22, 2025

Feature

You can now create an instance with both private services access and Private Service Connect enabled. You can also enable Private Service Connect on an existing private services access instance. This feature is now generally available ([GA](https://cloud.google.com/products#product-launch-stages)).

For more information, see [Configure both private services access and Private Service Connect](https://docs.cloud.google.com/sql/docs/mysql/configure-private-services-access-and-private-service-connect).

## May 15, 2025

Feature

You can now use [advanced disaster recovery (DR)](https://docs.cloud.google.com/sql/docs/mysql/intro-to-cloud-sql-disaster-recovery#advanced-dr) for your Private Service Connect (PSC) enabled Cloud SQL Enterprise Plus edition instances. With advanced DR, you can:

  * Designate a cross-region disaster recovery (DR) replica
  * Perform a cross-region replica failover for disaster recovery
  * Restore your original deployment by using zero-data loss switchover



You can also use switchover to simulate disaster recovery without data loss. For more information, see [Use advanced disaster recovery (DR)](https://docs.cloud.google.com/sql/docs/mysql/use-advanced-disaster-recovery). This feature is [generally available](https://cloud.google.com/products#product-launch-stages) (GA).

Feature

Cloud SQL for MySQL now supports minor version 8.0.42. To upgrade your existing instance to the new version, see [Upgrade the database minor version](https://docs.cloud.google.com/sql/docs/mysql/upgrade-minor-db-version).

## May 08, 2025

Change

If you create an instance using the Google Cloud Console, then the per-instance CA (`GOOGLE_MANAGED_INTERNAL_CA`) option is now the default [server certificate authority (CA) mode](https://docs.cloud.google.com/sql/docs/mysql/authorize-ssl#ca-hierarchies) for your Cloud SQL instance.

For users of the [Cloud SQL Auth Proxy](https://docs.cloud.google.com/sql/docs/mysql/sql-proxy): 

  * If the Cloud SQL instance to which you're connecting is using [shared certificate authority (CA)](https://docs.cloud.google.com/sql/docs/mysql/authorize-ssl#shared-regional-ca) for its `serverCaMode` setting, then on the client side, you must use Cloud SQL Auth Proxy version 2.13.0 or later.
  * If the Cloud SQL instance to which you're connecting is using [customer-managed CA](https://docs.cloud.google.com/sql/docs/mysql/authorize-ssl#customer-managed-ca) for its `serverCaMode` setting, then on the client side, you must use Cloud SQL Auth Proxy version 2.14.3 or later.



## May 02, 2025

Feature

You can now [set up custom DNS names by configuring the custom subject alternative name (SAN)](https://docs.cloud.google.com/sql/docs/mysql/custom-dns-name) for your instance. After you set up DNS name resolution, you can connect to your Cloud SQL instance using the custom DNS name instead of using an IP address. This feature is available only for instances that are configured with the [customer-managed certificate authority (CA)](https://docs.cloud.google.com/sql/docs/mysql/customer-managed-ca) (`CUSTOMER_MANAGED_CAS_CA`) option as its server CA mode.

Custom SAN configuration for instances is [generally available](https://cloud.google.com/products#product-launch-stages) (GA).

## May 01, 2025

Feature

Cloud SQL gives you the flexibility to choose between three [CA hierarchy options](https://docs.cloud.google.com/sql/docs/mysql/authorize-ssl#ca-hierarchies) when you [create a Cloud SQL instance](https://docs.cloud.google.com/sql/docs/mysql/create-instance).

You can choose between the per-instance CA (`GOOGLE_MANAGED_INTERNAL_CA`), the shared CA (`GOOGLE_MANAGED_CAS_CA`), or the customer-managed CA (`CUSTOMER_MANAGED_CAS_CA`) options as the server certificate authority (CA) mode for your instance. If you create an instance using the Google Cloud Console, then the shared CA option, (`GOOGLE_MANAGED_CAS_CA`), is the default configuration. If you create an instance using gcloud, the Cloud SQL Admin REST API, or Terraform, then the per-instance CA option (`GOOGLE_MANAGED_INTERNAL_CA`) is the default configuration.

The shared CA and customer-managed CA options are now [generally available](https://cloud.google.com/products#product-launch-stages) (GA).

## April 24, 2025

Feature

[Private Service Connect endpoint propagation](https://docs.cloud.google.com/sql/docs/mysql/about-private-service-connect#psc-endpoint-propagation) is now [generally available](https://cloud.google.com/products#product-launch-stages) (GA). You can use the Network Connectivity Center hub to propagate the Private Service Connect endpoints of your Cloud SQL instances in a VPC network.

## April 18, 2025

Change

Cloud SQL for MySQL 8.0.40 is now the default minor version. To upgrade your existing instance to the new version, see [Upgrade the database minor version](https://docs.cloud.google.com/sql/docs/mysql/upgrade-minor-db-version).

## April 09, 2025

Feature

Cloud SQL Enterprise Plus edition now supports a new machine series called the C4A machine series, which provides optimized price-performance and delivers predictable high performance for high demand Cloud SQL workloads. C4A uses a new type of storage called [Hyperdisk Balanced](https://docs.cloud.google.com/sql/docs/mysql/storage-options-overview), and offers up to 72 vCPUs and up to 576 GB memory. The C4A machine series is available in [Preview](https://cloud.google.com/products#product-launch-stages).

For more information about the C4A machine series and its availability, see [Machine series overview](https://docs.cloud.google.com/sql/docs/mysql/machine-series-overview).

Feature

Cloud SQL for Enterprise Plus edition supports [AI-assisted troubleshooting](https://docs.cloud.google.com/sql/docs/mysql/observe-troubleshoot-with-ai). With AI-assisted troubleshooting, you can resolve complex database performance issues like [slow queries](https://docs.cloud.google.com/sql/docs/mysql/troubleshoot-slow-queries) and [high load](https://docs.cloud.google.com/sql/docs/mysql/troubleshoot-high-database-load) for your instances in a guided manner. To use AI-assisted troubleshooting, you need [Gemini Cloud Assist](https://docs.cloud.google.com/gemini/docs/cloud-assist/overview) and [query insights for Enterprise Plus edition](https://docs.cloud.google.com/sql/docs/mysql/using-query-insights#enable-insights). AI-assisted troubleshooting is available in [Preview](https://cloud.google.com/products#product-launch-stages).

Feature

[Query insights for Cloud SQL Enterprise Plus edition](https://docs.cloud.google.com/sql/docs/mysql/using-query-insights#query-insights-for-enterprise-plus) is now generally available (GA) for your Cloud SQL Enterprise Plus edition for MySQL instances. Query insights for Cloud SQL Enterprise Plus edition offers fine-grained metrics such as wait events and granular query plan samples for faster root-cause analysis and intelligent index recommendations.

For more information, see [Use query insights to improve query performance](https://docs.cloud.google.com/sql/docs/mysql/using-query-insights).

## April 08, 2025

Feature

Cloud SQL for MySQL 8.4.3 is upgraded to MySQL 8.4.4. For more information, see the [MySQL 8.4.4 Release Notes](https://dev.mysql.com/doc/relnotes/mysql/8.4/en/news-8-4-4.html).

## April 03, 2025

Feature

You can now integrate Cloud SQL for MySQL and Vertex AI (in [Preview](https://cloud.google.com/products#product-launch-stages)). This allows you to [invoke predictions](https://docs.cloud.google.com/sql/docs/mysql/invoke-online-predictions) and [generate vector embeddings](https://docs.cloud.google.com/sql/docs/mysql/understand-example-embedding-workflow) using models hosted in Vertex AI. To use this integration, update your instance to [`[MySQL version].R20250304.00_01`](https://docs.cloud.google.com/sql/docs/mysql/maintenance-changelog).

For more information, see [Integrate Cloud SQL with Vertex AI](https://docs.cloud.google.com/sql/docs/mysql/integrate-cloud-sql-with-vertex-ai).

## March 31, 2025

Feature

Cloud SQL now supports Managed Connection Pooling (MCP) in [Preview](https://cloud.google.com/products#product-launch-stages), which lets you scale your workloads by optimizing resource utilization for your Cloud SQL instances using pooling. To use Managed Connection Pooling, update your instance to [`[MySQL version].R20250302.00_04`](https://docs.cloud.google.com/sql/docs/mysql/maintenance-changelog).

For more information, see [Managed Connection Pooling overview](https://docs.cloud.google.com/sql/docs/mysql/managed-connection-pooling).

## March 25, 2025

Feature

Cloud SQL read pools provide operational simplicity and scaling for your large read workloads.

Read pools provide a single endpoint in front of up to 20 read pool nodes and automatically load balance traffic.

You can scale your read pool in several ways:

  * **Scale in or out** : scale load balancing capacity horizontally by modifying the number of read pool nodes in the read pool. Each read pool supports up to 20 read pool nodes.
  * **Scale up or down** : scale load balancing capacity vertically by modifying the machine type associated with a read pool node. Once defined, configuration is uniformly applied across each read pool node in the read pool.



For more information, see [About read pools](https://docs.cloud.google.com/sql/docs/mysql/about-read-pools).

## March 24, 2025

Feature

Cloud SQL now lets you retain existing backups after an instance is deleted. These consist of on-demand and automatic backups created when the instance was live. For more information, see [Retained backups](https://docs.cloud.google.com/sql/docs/mysql/backup-recovery/backups#retained-backups).

## March 18, 2025

Feature

You can now [use PITR to restore a Cloud SQL for MySQL instance that isn't available](https://docs.cloud.google.com/sql/docs/mysql/backup-recovery/restore#pitr-instance-not-available).

## March 10, 2025

Feature

Cloud SQL for MySQL introduces a set of improvements that adjust MySQL configurations dynamically based on workload demands and underlying infrastructure to optimize write performance and reduce latency. By default these improvements are enabled for all new [Cloud SQL Enterprise Plus edition instances](https://docs.cloud.google.com/sql/docs/mysql/editions-intro) that you create or that you upgrade to from Cloud SQL Enterprise edition. Existing Cloud SQL Enterprise Plus instances that are updated with maintenance version `[MySQL_version].R20250304.00_01` will also enable these improvements automatically. 

For more information about these improvements, see [Configure database flags](https://docs.cloud.google.com/sql/docs/mysql/flags#tips-optimized-write).

## March 04, 2025

Feature

[Cloud SQL Enterprise edition](https://docs.cloud.google.com/sql/docs/mysql/instance-settings) now supports the `europe-north2` (Stockholm) region.

Feature

Cloud SQL for MySQL now supports minor version 8.0.41. To upgrade your existing instance to the new version, see [Upgrade the database minor version](https://docs.cloud.google.com/sql/docs/mysql/upgrade-minor-db-version).

## February 26, 2025

Feature

You can now include replicas when you perform an in-place major version upgrade using gcloud or the Cloud SQL Admin API. For more information, see [Upgrade the database major version in-place](https://docs.cloud.google.com/sql/docs/mysql/upgrade-major-db-version-inplace#include-replicas).

## February 20, 2025

Feature

You can now create a final backup of your data before you delete a Cloud SQL instance. You can use the final backup to restore your data to a new instance. This way, you can recover your data after you delete the instance. For more information, see [About Cloud SQL backups](https://docs.cloud.google.com/sql/docs/mysql/backup-recovery/backups#final-backups).

## February 13, 2025

Feature

Cloud SQL for MySQL lets you recreate a lagging replica when replication falls behind a predefined length of time. For more information, see [Recreate lagging replica](https://docs.cloud.google.com/sql/docs/mysql/replication/replication-lag#recreate_lagging_replica). This feature is in Preview.

## February 11, 2025

Feature

Cloud SQL for MySQL vector search is now generally available. After you store vector embeddings in a table, you can perform K-nearest neighbor (KNN) searches against your vector dataset. You can also add a vector search index to perform approximate nearest neighbor (ANN) searches.

For more information, see [Vector search](https://docs.cloud.google.com/sql/docs/mysql/vector-search).

Feature

You can now use a custom DNS name to connect to your Cloud SQL instances by adding a custom subject alternative name (SAN) to your Cloud SQL instances. This feature is available for instances that are configured with Customer Managed CAS CA.. For more information, see [Create instances](https://docs.cloud.google.com/sql/docs/mysql/create-instance).

You can also add, modify, and remove a custom SAN for existing Cloud SQL instances. For more information, see [Edit instances](https://docs.cloud.google.com/sql/docs/mysql/edit-instance). 

This feature is available in [Preview](https://cloud.google.com/products#product-launch-stages).

## February 05, 2025

Feature

You can now configure customer-managed CA (`CUSTOMER_MANAGED_CAS_CA`) as the server certificate authority (CA) mode when you create a Cloud SQL instance. With customer-managed CA mode, you set up your own CA pool and CA in [Certificate Authority Service](https://docs.cloud.google.com/certificate-authority-service/docs/ca-service-overview). This option lets you establish your own CA hierarchy and manage the rotation of CA certificates for your Cloud SQL instances to help you meet your regulatory compliance needs. 

To use the customer-managed CA option in Cloud SQL, see [Use a customer-managed certificate authority (CA)](https://docs.cloud.google.com/sql/docs/mysql/customer-managed-ca). For more information about server CA mode options, see [Certificate authority (CA) hierarchies](https://docs.cloud.google.com/sql/docs/mysql/authorize-ssl#ca-hierarchies). The customer-managed CA feature is in [Preview](https://cloud.google.com/products#product-launch-stages).

## February 01, 2025

Announcement

All Cloud SQL for MySQL 5.6 and 5.7 instances are running community end-of-life (EOL) major versions and are now enrolled in Cloud SQL extended support. 

**IMPORTANT** : Extended support is a paid service and is an addition to the current cost of your instance. Charges for extended support are waived from February 1, 2025 through April 30, 2025. Starting on May 1, 2025, all instances enrolled in extended support will be charged. To learn more about the benefits of extended support and pricing, see [Extended support for Cloud SQL](https://docs.cloud.google.com/sql/docs/mysql/extended-support).

## January 14, 2025

Feature

You can now migrate data from Microsoft Azure to Cloud SQL. For more information, see [Configure Cloud SQL and the external server for replication](https://docs.cloud.google.com/sql/docs/mysql/replication/configure-replication-from-external).

## January 13, 2025

Deprecated

As of January 13, 2025, the legacy configuration for high availability (HA) is deprecated for all Cloud SQL for MySQL instances. You can no longer create instances with the legacy HA configuration, and you can no longer enable the legacy HA configuration on existing instances. In addition, after January 13, 2025, legacy HA instances are no longer covered by the [Cloud SQL SLA](https://cloud.google.com/sql/sla).

We recommend that you update your remaining legacy HA instances as soon as possible to the current HA configuration. You can do so by following the instructions in [Update an instance from legacy to current high availability](https://docs.cloud.google.com/sql/docs/mysql/configure-legacy-ha#update-from-legacy).

Starting on May 1, 2025, Cloud SQL will begin updating any instances that use the legacy high availability configuration to use the current regional persistent disk-based high availability configuration automatically.

## December 20, 2024

Feature

You can now enable query insights for Cloud SQL Enterprise Plus edition. When you enable query insights for Enterprise Plus, you can access additional features in query insights such as 30 days of metrics retention, granular query plan details, and a higher query length limit. 

For more information, see [Use query insights to improve query performance](https://docs.cloud.google.com/sql/docs/mysql/using-query-insights#query-insights-for-enterprise-plus). Query insights for Cloud SQL Cloud SQL Enterprise Plus edition is in [Preview](https://cloud.google.com/products#product-launch-stages).

## December 18, 2024

Feature

Cloud SQL for MySQL 8.4.0 is upgraded to MySQL 8.4.3. For more information, see the [MySQL 8.4.3 Release Notes](https://dev.mysql.com/doc/relnotes/mysql/8.4/en/news-8-4-3.html), the [MySQL 8.4.2 Release Notes](https://dev.mysql.com/doc/relnotes/mysql/8.4/en/news-8-4-2.html), and the [MySQL 8.4.1 Release Notes](https://dev.mysql.com/doc/relnotes/mysql/8.4/en/news-8-4-1.html).

## December 10, 2024

Change

Cloud SQL now offers notifications for maintenance that's either started or completed. See the [Overview of maintenance on Cloud SQL instances](https://docs.cloud.google.com/sql/docs/mysql/maintenance#notifications). To find out how to sign up for notifications and check your instances for upcoming maintenance, see [Find and set maintenance windows](https://docs.cloud.google.com/sql/docs/mysql/set-maintenance-window).

## December 05, 2024

Feature

[Cloud SQL Enterprise Plus edition](https://docs.cloud.google.com/sql/docs/editions-intro) now supports the following regions:

  * `africa-south1` (Johannesburg)
  * `asia-east2` (Hong Kong)
  * `europe-west10` (Berlin)



## December 04, 2024

Feature

Cloud SQL for MySQL now supports minor version 8.0.40. To upgrade your existing instance to the new version, see [Upgrade the database minor version](https://docs.cloud.google.com/sql/docs/mysql/upgrade-minor-db-version).

## December 03, 2024

Feature

You can now use the Network Connectivity Center hub to [propagate Private Service Connect endpoints](https://docs.cloud.google.com/sql/docs/mysql/about-private-service-connect#psc-endpoint-propagation) of Cloud SQL instances in a VPC network. All endpoints in this network become accessible transitively to other spoke VPC networks through the hub. This feature is available in [Preview](https://cloud.google.com/products#product-launch-stages).

## November 27, 2024

Feature

You can now create instances with both private services access and Private Service Connect enabled for them. You can also enable Private Service Connect for existing private services access instances. This feature is available in [Preview](https://cloud.google.com/products#product-launch-stages). For more information, see [Configure both private services access and Private Service Connect](https://docs.cloud.google.com/sql/docs/mysql/configure-private-services-access-and-private-service-connect).

## November 20, 2024

Feature

You can now authenticate to Cloud SQL Studio by using [IAM database authentication](https://docs.cloud.google.com/sql/docs/mysql/iam-authentication#iam-db-auth).

For more information about authentication in Cloud SQL Studio, see [Manage your data using Cloud SQL Studio](https://docs.cloud.google.com/sql/docs/mysql/manage-data-using-studio#authentication).

## November 19, 2024

Feature

For [Cloud SQL Enterprise Plus edition](https://docs.cloud.google.com/sql/docs/mysql/editions-intro) instances, advanced disaster recovery (DR) is now [generally available (GA)](https://cloud.google.com/products#product-launch-stages). For more information, see [Advanced disaster recovery (DR)](https://docs.cloud.google.com/sql/docs/mysql/intro-to-cloud-sql-disaster-recovery#advanced-dr) and [Use advanced disaster recovery (DR)](https://docs.cloud.google.com/sql/docs/mysql/use-advanced-disaster-recovery).

Feature

The write endpoint feature is now available in [Preview](https://cloud.google.com/products#product-launch-stages). This endpoint is a global domain name service (DNS) name. This name resolves to the IP address of the current primary Cloud SQL instance that's enabled with private services access.

By using a write endpoint, you can avoid having to make application connection changes after performing a switchover or replica failover operation to test or mitigate a regional failure. For more information, see [Configure private IP](https://docs.cloud.google.com/sql/docs/mysql/configure-private-ip#connect-write-endpoint).

## November 18, 2024

Feature

Cloud SQL now supports near-zero downtime for infrequent scale downs (once every three hours) of the compute size (vCPU, memory) of your Cloud SQL Enterprise Plus edition primary instance.

For more information, see [Availability in Cloud SQL](https://docs.cloud.google.com/sql/docs/mysql/availability#planned_operations_with_near-zero_downtime).

Feature

Cloud SQL now supports near-zero downtime when you enable or disable [data cache](https://docs.cloud.google.com/sql/docs/mysql/data-cache) for Cloud SQL Enterprise Plus edition primary instances. For more information, see [Availability in Cloud SQL](https://docs.cloud.google.com/sql/docs/mysql/availability#planned_operations_with_near-zero_downtime).

Feature

Support for the [`northamerica-south1`](https://docs.cloud.google.com/sql/docs/mysql/locations) (Mexico) region.

## November 14, 2024

Feature

You can now create custom organization policies for the [`BackupRun`](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/backupRuns) resource in Cloud SQL instances. In addition, more fields in the [`Instances`](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/instances) resource are available to create custom organization policies. For more information, see [Add custom organization policies](https://docs.cloud.google.com/sql/docs/mysql/org-policy/custom-org-policy).

## November 12, 2024

Feature

You can now have Cloud SQL create a Private Service Connect endpoint automatically instead of creating the endpoint manually after the instance is created. You use this endpoint to access a Cloud SQL instance through a VPC network. For more information, see [Connect to an instance using Private Service Connect](https://docs.cloud.google.com/sql/docs/mysql/configure-private-service-connect#create-endpoint-automatically). This feature is available in [Preview](https://cloud.google.com/products#product-launch-stages).

## November 04, 2024

Feature

You can now [view the size of a backup](https://docs.cloud.google.com/sql/docs/mysql/backup-recovery/backing-up#view-backup-size) for a Cloud SQL instance.

## October 25, 2024

Feature

When you run the [`backupRuns.GET` API](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/backupRuns/get) or the [`gcloud sql backups describe`](https://docs.cloud.google.com/sdk/gcloud/reference/sql/backups/describe) command, the `maxChargeableBytes` parameter now appears in the response. This parameter contains the maximum number of bytes that you can be charged for a backup.

## October 21, 2024

Feature

You can now create a read replica for an instance that has [private services access](https://docs.cloud.google.com/sql/docs/mysql/configure-private-services-access#configure-access) configured for it and [connector enforcement](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/instances#ConnectorEnforcement) enabled for it. For more information, see [Connect using Cloud SQL Language Connectors](https://docs.cloud.google.com/sql/docs/mysql/connect-connectors#enforce).

## October 16, 2024

Feature

Cloud SQL for MySQL now supports minor version 8.0.39. To upgrade your existing MySQL 8.0 instance to the new version, see [Upgrade the database minor version](https://docs.cloud.google.com/sql/docs/mysql/upgrade-minor-db-version).

## October 03, 2024

Feature

You can now configure server certificate authority (CA) mode when you create a Cloud SQL instance. With server CA mode, you have two options:

  * **Per-instance CA** : this is the default configuration. With this option, an internal CA dedicated to each Cloud SQL instance signs the server certificate for that instance.
  * **Shared CA** : with this option, the Cloud SQL instance uses a CA hierarchy consisting of a root CA and subordinate server CAs managed by Cloud SQL and hosted on Google Cloud Certificate Authority Service (CA Service). The subordinate server CAs in a region sign the server certificates and are shared across instances in the region. This option can be used only with MySQL 8.0.30 and later.



For more information about each option, see [Certificate authority (CA) hierarchies](https://docs.cloud.google.com/sql/docs/mysql/authorize-ssl#certificate_authority_ca_hierarchies). This feature is in [Preview](https://cloud.google.com/products#product-launch-stages).

## October 01, 2024

Feature

Cloud SQL for MySQL 8.4 is now generally available. For more information about the differences between MySQL 8.4 and MySQL 8.0, review [What Is New in MySQL 8.4 since MySQL 8.0](https://dev.mysql.com/doc/refman/8.4/en/mysql-nutshell.html).

By default, if you specify MySQL 8.4 as the version when you create a Cloud SQL instance (either primary or replica) using the gcloud CLI or the REST API, then the Cloud SQL edition is Enterprise Plus.

If you specify a version other than MySQL 8.4 or don't specify a version, then the default Cloud SQL edition of the instance is Enterprise.

For more information about the implementation of MySQL 8.4 in Cloud SQL, see the following topics:

  * [MySQL 8.4 authentication plugin default](https://docs.cloud.google.com/sql/docs/mysql/features#mysql84-auth-plugin-default)
  * [MySQL features unsupported for Cloud SQL](https://docs.cloud.google.com/sql/docs/mysql/features#unsupported-mysql-features)
  * [MySQL 8.4 user privileges (cloudsqlsuperuser)](https://docs.cloud.google.com/sql/docs/mysql/users#cloudsqlsuperuser-84)



To create a MySQL 8.4 instance in Cloud SQL, see [Create instances](https://docs.cloud.google.com/sql/docs/mysql/create-instance). Before you upgrade to MySQL 8.4, you must first upgrade to MySQL 8.0.37 or later. To perform a major version upgrade, see [Upgrade the database major version in-place](https://docs.cloud.google.com/sql/docs/mysql/upgrade-major-db-version-inplace). To perform a minor version upgrade of Cloud SQL for MySQL 8.0, see [Upgrade the database minor version](https://docs.cloud.google.com/sql/docs/mysql/upgrade-minor-db-version).

## September 16, 2024

Deprecated

Cloud SQL is discontinuing support for [legacy high availability (HA)](https://docs.cloud.google.com/sql/docs/mysql/configure-legacy-ha) instance configuration on January 6, 2025. After this date, you can't create Cloud SQL for MySQL instances with the legacy configuration for high availability. You also can't enable the legacy configuration for high availability on existing instances. Until January 6, 2025, legacy HA instances are still covered by the [Cloud SQL SLA](https://cloud.google.com/sql/sla). We recommend that you [upgrade your existing legacy HA instances](https://docs.cloud.google.com/sql/docs/mysql/configure-legacy-ha#update-from-legacy) to regional persistent disk HA instances as soon as possible and create new HA instances using regional persistent disk instead.

Starting on May 1, 2025, Cloud SQL will migrate any remaining instances that use the legacy HA configuration to the current HA configuration automatically.

## September 12, 2024

Feature

Cloud SQL now supports near-zero downtime planned maintenance on standalone Cloud SQL Enterprise Plus edition primary instances. In addition, you can also simulate near-zero downtime for planned maintenance events on standalone Cloud SQL Enterprise Plus edition primary instances.

For more information, see [About maintenance on Cloud SQL instances](https://docs.cloud.google.com/sql/docs/mysql/maintenance).

Feature

You can now upgrade the minor version of a Cloud SQL for MySQL Enterprise Plus edition instance with near-zero downtime. To upgrade the minor version of your Cloud SQL for MySQL 8.0 instance, see [Upgrade the minor version](https://docs.cloud.google.com/sql/docs/mysql/upgrade-minor-db-version).

Feature

You can now provide access to Cloud SQL Studio by granting a new IAM role, Cloud SQL Studio User (`roles/cloudsql.studioUser`), instead of using the Cloud SQL Admin IAM role.

For more information about using Cloud SQL Studio, see [Manage your data using Cloud SQL Studio](https://docs.cloud.google.com/sql/docs/mysql/manage-data-using-studio).

Feature

You can now upgrade your instances to Cloud SQL Enterprise Plus edition with near-zero downtime. To upgrade your instance, see [Upgrade an instance to Cloud SQL Enterprise Plus edition using in-place upgrade](https://docs.cloud.google.com/sql/docs/mysql/upgrade-cloud-sql-instance-to-enterprise-plus-in-place).

## September 03, 2024

Feature

When you clone your zonal instance, you can now specify a preferred zone for the instance. You can also specify preferred primary and secondary zones for your regional instance. If the zones for your instance go down in the future, then Cloud SQL can assign the preferred zones to the instance, and you don't experience downtime. For more information, see [Clone instances](https://docs.cloud.google.com/sql/docs/mysql/clone-instance).

## August 15, 2024

Announcement

Extended support pricing is now available for Cloud SQL for MySQL. To view pricing details, see [Cloud SQL pricing](https://cloud.google.com/sql/pricing#extended-support-pricing).

For more information about extended support, see [Extended support for Cloud SQL](https://docs.cloud.google.com/sql/docs/mysql/extended-support). 

For more information about extended support timelines, see [Database versions and version policies](https://docs.cloud.google.com/sql/docs/mysql/db-versions).

## July 31, 2024

Feature

Gemini in Databases assistance in Cloud SQL for MySQL is now available in [Preview](https://cloud.google.com/products#product-launch-stages) for query insights, system insights, index advisor, and active queries. You can use Gemini assistance to help you observe and troubleshoot your Cloud SQL resources. For more information, see [Observe and troubleshoot with Gemini assistance](https://docs.cloud.google.com/sql/docs/mysql/observe-troubleshoot-with-gemini).

## July 30, 2024

Feature

You can now use the gcloud CLI or the Cloud SQL Admin API to switch the storage location of transaction logs used for point-in-time recovery (PITR) on your instance from disk to Cloud Storage. For more information, see [Use point-in-time recovery](https://docs.cloud.google.com/sql/docs/mysql/backup-recovery/pitr) and [Switch transaction log storage to Cloud Storage](https://docs.cloud.google.com/sql/docs/mysql/backup-recovery/pitr#switch-to-gcs).

## July 29, 2024

Feature

Migrating your external MySQL 5.7 and 8.0 databases into Cloud SQL for MySQL by using Percona XtraBackup physical files is now [generally available](https://cloud.google.com/products#product-launch-stages) (GA).

For more information, see [Migrate to Cloud SQL from an XtraBackup physical file](https://docs.cloud.google.com/sql/docs/mysql/migrate-xtrabackup-physical-file).

## July 26, 2024

Feature

[IAM group authentication](https://docs.cloud.google.com/sql/docs/mysql/iam-authentication#iam-group-auth) is now generally available (GA) for Cloud SQL for MySQL. You can [add IAM groups to Cloud SQL instances](https://docs.cloud.google.com/sql/docs/mysql/add-manage-iam-users#add-iam-group-db) and manage database access at the group level. To use IAM group authentication, you must have `[MySQL version].R20230909.02_00` or later installed on your instance.

## July 25, 2024

Change

You can now upgrade the network architecture of a Cloud SQL instance that isn't enabled with [high-availability](https://docs.cloud.google.com/sql/docs/mysql/high-availability). The previous limitation on upgrading the network architecture of these instances is removed. To check whether your Cloud SQL instance has high availability enabled, see [Verify an instance's high availability configuration](https://docs.cloud.google.com/sql/docs/mysql/configure-ha#verify-ha).

For more information about upgrading your network architecture, see [Upgrade an instance to the new network architecture](https://docs.cloud.google.com/sql/docs/mysql/upgrade-cloud-sql-instance-new-network-architecture).

## July 18, 2024

Feature

You can now create custom organization policies for Cloud SQL instances. For more information, see [Add custom organization policies](https://docs.cloud.google.com/sql/docs/mysql/org-policy/custom-org-policy).

## July 16, 2024

Feature

Cloud SQL Studio is now [generally available](https://cloud.google.com/products#product-launch-stages). For more information, see [Manage your data using Cloud SQL Studio](https://docs.cloud.google.com/sql/docs/mysql/manage-data-using-studio).

Feature

You can now search for and manage your Cloud SQL resources by using [Dataplex Catalog](https://docs.cloud.google.com/dataplex/docs/catalog-overview). For more information about the integration of Cloud SQL and Dataplex Catalog, see [Manage your Cloud SQL resources using Dataplex Catalog](https://docs.cloud.google.com/sql/docs/mysql/dataplex-catalog-integration).

## July 02, 2024

Feature

[Cloud SQL Enterprise Plus edition](https://docs.cloud.google.com/sql/docs/editions-intro) now supports the southamerica-west1 (Santiago) region.

## June 24, 2024

Change

You can now upgrade the network architecture of Cloud SQL for MySQL instances that store transaction logs used for point-in-time recovery (PITR) in Cloud Storage. The previous limitation on upgrade of such instances is removed. To check where your MySQL instance stores its PITR logs, see [Check the storage location of transaction logs used for PITR](https://docs.cloud.google.com/sql/docs/mysql/backup-recovery/pitr#check-log-storage-location).

For more information about upgrading your network architecture, see [Upgrade an instance to the new network architecture](https://docs.cloud.google.com/sql/docs/mysql/upgrade-cloud-sql-instance-new-network-architecture).

## June 20, 2024

Feature

You can now use the `gcloud sql instances describe` command or the SQL Admin API to retrieve a list of database versions that are available to your MySQL instance for upgrade. For more information, see [Plan a major version upgrade](https://docs.cloud.google.com/sql/docs/mysql/upgrade-major-db-version-inplace#plan-upgrade) and [Upgrade the database minor version](https://docs.cloud.google.com/sql/docs/mysql/upgrade-minor-db-version#before_you_upgrade).

## June 13, 2024

Feature

Cloud SQL for MySQL now supports minor version 8.0.37. To upgrade your existing instance to the new version, see [Upgrade the database minor version](https://docs.cloud.google.com/sql/docs/mysql/upgrade-minor-db-version).

## June 10, 2024

Feature

You can now choose to receive a maintenance notification 5 weeks before the maintenance update of your Cloud SQL instance is scheduled to occur. This option is named **Week 5**.

In addition, some labels in the Google Cloud Console have been renamed to align with this new option:

  * **Order of update** is renamed to **Maintenance timing**
  * **Earlier** is renamed to **Week 1**
  * **Later** is renamed to **Week 2**



For more information, see [Maintenance settings](https://docs.cloud.google.com/sql/docs/mysql/maintenance#management) and [Find and set maintenance windows](https://docs.cloud.google.com/sql/docs/mysql/set-maintenance-window).

## May 29, 2024

Announcement

Cloud SQL for MySQL major versions that have reached community end-of-life (EOL) will receive extended support starting on February 1, 2025. For more information about extended support, see [Extended support for Cloud SQL](https://docs.cloud.google.com/sql/docs/mysql/extended-support).

For more information about extended support timelines, see [Database versions and version policies](https://docs.cloud.google.com/sql/docs/mysql/db-versions).

## April 09, 2024

Feature

The following [Gemini in Databases](https://docs.cloud.google.com/gemini/docs/databases/overview) features are now available in Public Preview:

  * [Database Center](https://docs.cloud.google.com/database-center/docs/overview): an AI-assisted dashboard that gives you one centralized view across your entire database fleet.
  * [Cloud SQL Studio](https://docs.cloud.google.com/sql/docs/mysql/manage-data-using-studio): lets authorized users interact directly with the SQL database and run SQL queries from the Google Cloud console to access and manipulate data.
  * [Monitor active queries](https://docs.cloud.google.com/sql/docs/mysql/monitor-active-queries): monitor and troubleshoot the queries that are active in your database.
  * [Index advisor](https://docs.cloud.google.com/sql/docs/mysql/index-advisor-overview): a fully managed index advisor that tracks the queries your database handles regularly.
  * 4-week query metric retention in the [Query Insights dashboard](https://docs.cloud.google.com/sql/docs/mysql/using-query-insights).
  * 17 new database insight recommendations.



To learn how to enable and activate Gemini in Databases, see [Set up Gemini in Databases](https://docs.cloud.google.com/gemini/docs/databases/set-up-gemini).

Feature

Cloud SQL for MySQL now supports the storage of vector embeddings in MySQL 8.0.36 and later databases. To use this feature, update your instance to `MySQL 8.0.36.R20240401.03_00` or later.

After you store vector embeddings in your database, you can then perform K-nearest neighbor (KNN) searches on the dataset along with the rest of your data. Cloud SQL for MySQL also supports the creation of vector search indexes for several different index types using approximate nearest neighbor (ANN) search.

For more information, see [Working with vector embeddings using Cloud SQL for MySQL](https://docs.cloud.google.com/sql/docs/mysql/generate-manage-vector-embeddings). This feature is in [Preview](https://cloud.google.com/products#product-launch-stages).

## April 08, 2024

Feature

[Cloud SQL Enterprise Plus edition](https://docs.cloud.google.com/sql/docs/mysql/editions-intro) primary instances with high availability (HA) now require less than one second of downtime for [planned maintenance](https://docs.cloud.google.com/sql/docs/mysql/maintenance#nearzero).

## April 04, 2024

Feature

For [Cloud SQL Enterprise Plus edition](https://docs.cloud.google.com/sql/docs/mysql/editions-intro), you can now use advanced disaster recovery (DR) to simplify recovery and fallback processes after you perform a cross-regional failover. With advanced DR, you can: 

  * Designate a cross-region disaster recovery (DR) replica
  * Perform replica failover
  * Restore your original deployment by using zero data loss switchover



You can also use switchover to simulate disaster recovery without data loss. 

For more information, see [Advanced disaster recovery (DR)](https://docs.cloud.google.com/sql/docs/mysql/intro-to-cloud-sql-disaster-recovery#advanced-dr) and [Use advanced disaster recovery (DR)](https://docs.cloud.google.com/sql/docs/mysql/use-advanced-disaster-recovery). This feature is in [Preview](https://cloud.google.com/products#product-launch-stages).

## April 03, 2024

Feature

You can now migrate your external MySQL 5.7 and 8.0 databases into Cloud SQL for MySQL by using Percona XtraBackup physical files. This feature is in [Preview](https://cloud.google.com/products#product-launch-stages).

For more information, see [Migrate to Cloud SQL from an XtraBackup physical file](https://docs.cloud.google.com/sql/docs/mysql/migrate-xtrabackup-physical-file).

## April 02, 2024

Feature

You can now scale up the compute size (vCPU, memory) of a [Cloud SQL Enterprise Plus edition](https://docs.cloud.google.com/sql/docs/mysql/editions-intro) primary instance with near-zero downtime.

## April 01, 2024

Change

If your Cloud SQL Enterprise edition instance stores the transaction logs used for point-in-time recovery (PITR) on disk, then when you do an in-place upgrade to Cloud SQL Enterprise Plus edition, the storage location for the transaction logs is switched to Cloud Storage. For more information, see [Upgrade an instance to Cloud SQL Enterprise Plus edition by using in-place upgrade](https://docs.cloud.google.com/sql/docs/mysql/upgrade-cloud-sql-instance-to-enterprise-plus-in-place).

To check where your instance stores the transaction logs used for PITR, see [Use point-in-time recovery (PITR)](https://docs.cloud.google.com/sql/docs/mysql/backup-recovery/pitr#check-log-storage-location).

## March 28, 2024

Feature

You can now simulate a planned maintenance update with near-zero downtime on your [Cloud SQL Enterprise Plus](https://docs.cloud.google.com/sql/docs/mysql/editions-intro) primary instance without updating your database. For more information, see [About maintenance on Cloud SQL instances](https://docs.cloud.google.com/sql/docs/mysql/maintenance#simulate-zdt).

## March 25, 2024

Feature

Private Service Connect now includes support for [cross-region read replicas](https://docs.cloud.google.com/sql/docs/mysql/replication/create-replica#create-read-replica-cloud-sql-instance-psc-enabled). You can also [choose an availability type](https://docs.cloud.google.com/sql/docs/mysql/configure-ha) (REGIONAL or ZONAL) for Private Service Connect-enabled instances. Both features are in [GA](https://cloud.google.com/products#product-launch-stages).

## March 19, 2024

Feature

[Cloud SQL Enterprise Plus edition](https://docs.cloud.google.com/sql/docs/editions-intro) now supports the me-central2 (Dammam) region.

## March 05, 2024

Feature

You can now upgrade network architecture for your HA-enabled instances in a region, even if you have multiple instances in your network and region. For more information, see [Upgrade an instance to the new network architecture](https://docs.cloud.google.com/sql/docs/mysql/upgrade-cloud-sql-instance-new-network-architecture).

## February 13, 2024

Announcement

A new maintenance version rollout is currently underway for all supported MySQL versions.

If you have configured a maintenance window for your instance, then the updates will occur according to the timeframe that you set in the window. Otherwise, the updates will occur within the next few weeks. The new maintenance version is [MySQL version].R20240207.00_00.

To learn how to check your maintenance version, see [Self-service maintenance](https://docs.cloud.google.com/sql/docs/mysql/self-service-maintenance#before-you-begin). To find your maintenance window or to manage maintenance updates, see [Find and set maintenance windows](https://docs.cloud.google.com/sql/docs/mysql/set-maintenance-window).

Change

In the new maintenance version [MySQL version].R20240207.00_00, the default value of the `performance_schema` flag for all MySQL 8.0 instances with more than 15 GB of RAM will be set to `on`. Previously, the default of `on` for MySQL 8.0 only applied to 8.0.26 and later. This change applies to new and existing MySQL 8.0 instances. For more information about this flag, see [supported flags](https://docs.cloud.google.com/sql/docs/mysql/flags#list-flags-mysql).

## February 09, 2024

Feature

Cloud SQL now automatically updates your read replicas when you perform self-service maintenance on the primary instance. For more information, see [Self-service maintenance](https://docs.cloud.google.com/sql/docs/mysql/self-service-maintenance).

## February 08, 2024

Feature

Cloud SQL now supports near-zero downtime planned maintenance on HA-enabled Cloud SQL Enterprise Plus instances with all combinations of public IP connectivity.

## February 06, 2024

Feature

Cloud SQL for MySQL now supports minor version 8.0.36. To upgrade your existing instance to the new version, see [Upgrade the database minor version](https://docs.cloud.google.com/sql/docs/mysql/upgrade-minor-db-version).

## February 01, 2024

Feature

Private Service Connect now includes support for cross-region read replicas. You can also choose an availability type (REGIONAL or ZONAL) for Private Service Connect-enabled instances. Both features are in [Preview](https://cloud.google.com/products#product-launch-stages). 

For more information, see [Connect to an instance using Private Service Connect](https://docs.cloud.google.com/sql/docs/mysql/configure-private-service-connect).

## January 31, 2024

Feature

Support for [africa-south1](https://docs.cloud.google.com/sql/docs/mysql/locations) (Johannesburg) region.

## January 30, 2024

Feature

You can now use the [MySQL Shell](https://dev.mysql.com/doc/mysql-shell/8.0/en/) `dumpInstance` and `loadDump` utilities to export and import data for multiple files in parallel. For more information, see [Export and import files in parallel](https://docs.cloud.google.com/sql/docs/mysql/import-export/import-export-parallel).

## January 25, 2024

Feature

[Cloud SQL Enterprise Plus edition](https://docs.cloud.google.com/sql/docs/editions-intro) now supports the following regions:

  * asia-northeast2 (Osaka)
  * asia-south2 (Delhi)
  * europe-north1 (Finland)
  * europe-southwest1 (Madrid)
  * us-east5 (Columbus)
  * us-south1 (Dallas)



## January 12, 2024

Feature

Cloud SQL for MySQL now supports setting microsecond time periods for the following flag on MySQL 5.7 and MySQL 8.0: 

  * innodb_flush_log_at_timeout



For more information about this flag, see [supported flags](https://docs.cloud.google.com/sql/docs/mysql/flags#list-flags-mysql).

**Note** : The data type for the innodb_flush_log_at_timeout flag has changed from an unsigned integer to a double.

## December 19, 2023

Feature

You can now specify the SSL mode of your Cloud SQL for MySQL instances. To use SSL mode, you must use maintenance version [MySQL version].R20230909.02_00 or later. For more information, see [Enforce SSL/TLS encryption](https://docs.cloud.google.com/sql/docs/mysql/configure-ssl-instance#enforcing-ssl).

## December 18, 2023

Feature

Cloud SQL for MySQL now supports the following flags for MySQL 8.0:

  * innodb_buffer_pool_dump_now
  * innodb_buffer_pool_load_abort
  * innodb_buffer_pool_load_now



For more information about these flags, see [supported flags](https://docs.cloud.google.com/sql/docs/mysql/flags#list-flags-mysql).

Feature

[Cloud SQL Enterprise Plus edition](https://docs.cloud.google.com/sql/docs/mysql/editions-intro) now supports the following regions:

  * europe-west8 (Milan)
  * europe-west12 (Turin)
  * us-west4 (Las Vegas)



Announcement

Cloud SQL for MySQL has completed the upgrade to MySQL 5.7.44.

## December 14, 2023

Feature

You can now use Database Migration Service to [migrate data](https://docs.cloud.google.com/sql/docs/mysql/migrate-data-to-cloud-sql-instance) to an existing Cloud SQL instance that was created using Terraform or other Infrastructure-As-Code (IaC) Tools.

## December 13, 2023

Feature

You can now use the `cloudsql_ignore_innodb_encryption` flag to ignore InnoDB table encryption when you migrate instances to Cloud SQL. The flag is supported in MySQL 8.0 for Cloud SQL. For more information, see [Supported flags](https://docs.cloud.google.com/sql/docs/mysql/flags#list-flags-mysql).

## December 08, 2023

Feature

You can now upgrade your Cloud SQL instances to use the new network architecture to get additional capabilities not available in the old network architecture. For more information, see [Upgrade an instance to the new network architecture](https://docs.cloud.google.com/sql/docs/mysql/upgrade-cloud-sql-instance-new-network-architecture).

Feature

You can now configure Cloud SQL for MySQL instances for [IAM group authentication](https://docs.cloud.google.com/sql/docs/mysql/iam-authentication#iam-group-auth). IAM group authentication requires MySQL 8.0 and R20230909.02_00 or later. This feature is in [Preview](https://cloud.google.com/products#product-launch-stages).

## December 06, 2023

Feature

The rollout of the following MySQL versions is currently underway:

MySQL 5.7.43 is upgraded to MySQL 5.7.44. For more information, see [MySQL 5.7 Release Notes.](https://dev.mysql.com/doc/relnotes/mysql/5.7/en/news-5-7-44.html)

If you use a maintenance window, then the updates to the minor versions happen according to the timeframe that you set in the window. Otherwise, the updates occur within the next few weeks. The new maintenance version is [MySQL version].R20231105.01_00. The details of the security fixes applied as part of this release are published in the [MySQL maintenance changelog](https://docs.cloud.google.com/sql/maintenance-changelog).

To learn how to check your maintenance version, see [Self-service maintenance](https://docs.cloud.google.com/sql/docs/mysql/self-service-maintenance#before_you_begin/self-service-maintenance). To find your maintenance window or to manage maintenance updates, see [Find and set maintenance windows](https://docs.cloud.google.com/sql/docs/mysql/set-maintenance-window).

## November 17, 2023

Feature

Cloud SQL now supports migrating data to an instance that already exists. You can create the instance by using Terraform or other Infrastructure-As-Code (IaC) Tools. After creating the instance, use the [demote](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/instances/demote) API to migrate data to it. This API demotes an existing standalone instance to be a Cloud SQL read replica for an external database server.

Feature

Cloud SQL for MySQL now supports minor version 8.0.35. To upgrade your existing instance to the new version, see [Upgrade the database minor version](https://docs.cloud.google.com/sql/docs/mysql/upgrade-minor-db-version).

## November 10, 2023

Feature

You can now upgrade Enterprise edition instances to Enterprise Plus edition in place with minimal disruption. Similarly, you can also switch from Enterprise Plus edition to Enterprise edition in place. For more information, see [Upgrade an instance by using in-place upgrade](https://docs.cloud.google.com/sql/docs/mysql/upgrade-cloud-sql-instance-to-enterprise-plus-in-place).

## November 06, 2023

Feature

[Cloud SQL Enterprise Plus edition](https://docs.cloud.google.com/sql/docs/editions-intro) now supports asia-southeast2 (Jakarta).

## October 17, 2023

Announcement

Cloud SQL for MySQL has completed the upgrade to MySQL 5.7.43.

Feature

Cloud SQL supports [InnoDB page compression](https://dev.mysql.com/doc/refman/8.0/en/innodb-page-compression.html) for MySQL 5.7 and MySQL 8.0 and later.

## October 02, 2023

Change

For Cloud SQL Enterprise edition and Cloud SQL Enterprise Plus edition, you can [restore backups across instances of different editions](https://docs.cloud.google.com/sql/docs/mysql/backup-recovery/restore).

## September 26, 2023

Feature

Cloud SQL supports the preview version of the enable-high-availability recommender. This service proactively generates recommendations that help you bring your important instances within SLA by providing data redundancy. This might be helpful during a zonal outage or when an instance runs out of memory. For more information, see [Improve instance reliability by enabling high availability](https://docs.cloud.google.com/sql/docs/mysql/recommender-enable-ha).

## September 25, 2023

Feature

All Cloud SQL for MySQL Enterprise Plus edition instances now support up to 35 days of retained transaction logs for [point-in-time recovery](https://docs.cloud.google.com/sql/docs/mysql/backup-recovery/pitr).

Feature

The rollout of the following minor version is currently underway:

MySQL 5.7.42 is upgraded to MySQL 5.7.43. For more information, see [MySQL 5.7 Release Notes](https://dev.mysql.com/doc/relnotes/mysql/5.7/en/news-5-7-43.html).

If you use a maintenance window, then the updates to the minor versions happen according to the timeframe that you set in the window. Otherwise, the updates occur within the next few weeks. The new maintenance version is `[MySQL version].R20230909.02_00`. The details of the security fixes applied as part of this release will be published in the [MySQL maintenance changelog](https://docs.cloud.google.com/sql/maintenance-changelog). 

To learn how to check your maintenance version, see [Self-service maintenance](https://docs.cloud.google.com/sql/docs/mysql/self-service-maintenance#before_you_begin/self-service-maintenance). To find your maintenance window or to manage maintenance updates, see [Find and set maintenance windows](https://docs.cloud.google.com/sql/docs/mysql/set-maintenance-window).

## September 19, 2023

Feature

Support for [me-central2 (Dammam)](https://docs.cloud.google.com/sql/docs/mysql/locations) region.

## August 22, 2023

Feature

Support for [europe-west10 (Berlin)](https://docs.cloud.google.com/sql/docs/mysql/locations) region.

## August 21, 2023

Feature

[Private Service Connect](https://docs.cloud.google.com/sql/docs/mysql/configure-private-service-connect) is now GA for Cloud SQL for MySQL. This solution allows you to connect to a Cloud SQL instance from multiple VPC networks that belong to different groups, teams, projects, or organizations.

## August 18, 2023

Feature

[Cloud SQL Enterprise Plus edition](https://docs.cloud.google.com/sql/docs/editions-intro) now supports four new regions: 

  * europe-central2 (Warsaw)
  * europe-west9 (Paris)
  * southamerica-east1 (San Paulo)
  * us-west1 (Oregon)



Feature

Cloud SQL for MySQL now supports minor version 8.0.34. To upgrade your existing instance to the new version, see [Upgrade the database minor version](https://docs.cloud.google.com/sql/docs/mysql/upgrade-minor-db-version).

## August 17, 2023

Feature

You can now [re-encrypt an existing Cloud SQL CMEK-enabled primary instance or replica](https://docs.cloud.google.com/sql/docs/mysql/configure-cmek#reencrypt) with a new primary key version.

Feature

You can now retain up to [35 days of retention logs](https://docs.cloud.google.com/sql/docs/mysql/backup-recovery/pitr#log-storage-for-pitr) for your [Cloud SQL for MySQL Enterprise Plus edition](https://docs.cloud.google.com/sql/docs/editions-intro) instances when using point-in-time recovery.

Feature

Cloud SQL for MySQL now supports storage of [point-in-time recovery](https://docs.cloud.google.com/sql/docs/mysql/backup-recovery/restore#tips-pitr) logs in [Cloud storage](https://docs.cloud.google.com/storage/docs).

## August 11, 2023

Feature

[Cloud SQL Enterprise Plus edition](https://docs.cloud.google.com/sql/docs/mysql/editions-intro) now supports the asia-northeast3 (Seoul) region.

## August 09, 2023

Feature

You can now upgrade a Cloud SQL for MySQL instance to Cloud SQL Enterprise Plus edition by using [IP allowlists](https://docs.cloud.google.com/sql/docs/mysql/upgrade-cloud-sql-instance-to-enterprise-plus-ip-allowlists) and [VPC Peering](https://docs.cloud.google.com/sql/docs/mysql/upgrade-cloud-sql-instance-to-enterprise-plus-vpc-peering).

## August 03, 2023

Feature

Cloud SQL now supports multiple categories of API rate quotas. Rate quotas for each category are imposed per minute, per project, per region, and per user. For more information about rate quotas for each category, see [Quotas and limits](https://docs.cloud.google.com/sql/docs/mysql/quotas).

Feature

The [Cloud SQL Node.js Language Connector](https://docs.cloud.google.com/static/sql/docs/mysql/connect-connectors#node.js) is now available for public preview.

## August 01, 2023

Feature

You can now [migrate](https://docs.cloud.google.com/sql/docs/mysql/replication/managed-import-replication-from-external) large MySQL databases from external sources to Cloud SQL for MySQL faster using [Database Migration Service](https://docs.cloud.google.com/database-migration/docs/mysql/create-migration-job).

## July 18, 2023

Feature

Cloud SQL now supports [default maintenance windows](https://docs.cloud.google.com/sql/docs/mysql/maintenance#default-windows) for your instances. With this release, an instance without a user-specified maintenance window is maintained outside of the typical business hours for the time zone that the instance is deployed in.

## July 12, 2023

Feature

Cloud SQL now offers two editions of Cloud SQL to support your various business and application needs: **Cloud SQL Enterprise Plus edition** and **Cloud SQL Enterprise edition**. Each edition provides different performance and availability characteristics to meet the needs of your applications. 

Cloud SQL Editions are only available for Cloud SQL for MySQL and Cloud SQL for PostgreSQL. 

For more information about Cloud SQL editions, see [Introduction to Cloud SQL editions](https://docs.cloud.google.com/sql/docs/editions-intro).

## July 11, 2023

Feature

Cloud SQL now supports [cancelling the import and export of data](https://docs.cloud.google.com/sql/docs/mysql/import-export/cancel-import-export) into Cloud SQL for MySQL instances.

Feature

MySQL 5.7.40 has been upgraded to 5.7.42. For more information, see [MySQL 5.7 release notes](https://dev.mysql.com/doc/relnotes/mysql/5.7/en/).

## July 07, 2023

Feature

Cloud SQL for MySQL now supports up to 500,000 tables for instances that meet the minimum hardware requirements of 32+ cores and 200G+ memory. For more information, see [table limit](https://docs.cloud.google.com/sql/docs/mysql/quotas).

## July 06, 2023

Feature

Cloud SQL now supports [non-RFC 1918 IP address ranges](https://docs.cloud.google.com/sql/docs/mysql/configure-private-ip#non-rfc1918), including privately used public IP addresses. This enables you to create instances and replicas in a non-RFC 1918 IP address range. Additionally, you can connect to an instance from an application that is running in a non-RFC 1918 IP address range.

## June 30, 2023

Feature

For our preferred partners and allowlisted customers, [Private Service Connect](https://docs.cloud.google.com/sql/docs/mysql/configure-private-service-connect) is now available. This solution allows you to connect to a Cloud SQL instance from multiple VPC networks that belong to different groups, teams, projects, or organizations. To use Private Service Connect, contact your Technical Account Manager.

## June 15, 2023

Feature

The [Cloud SQL System insights dashboard](https://docs.cloud.google.com/sql/docs/mysql/use-system-insights) helps you detect and analyze system performance problems.

## May 22, 2023

Feature

Cloud SQL for MySQL now supports minor version 8.0.33. To upgrade your existing instance to the new version, see [Upgrade the database minor version](https://docs.cloud.google.com/sql/docs/mysql/upgrade-minor-db-version).

## May 19, 2023

Feature

Cloud SQL for MySQL has launched two database flags that impact the [Cloud SQL SLA](https://cloud.google.com/sql/sla): **innodb_flush_log_at_trx_commit** and **sync_binlog**. For more information about these flags, see [supported flags](https://docs.cloud.google.com/sql/docs/mysql/flags).

## May 16, 2023

Feature

The Cloud SQL Proxy Operator is now generally available. To learn more about the Cloud SQL Proxy Operator, see [About the Cloud SQL Proxy Operator](https://docs.cloud.google.com/sql/docs/mysql/connect-proxy-operator).

## April 19, 2023

Feature

Cloud SQL for MySQL now supports 40+ new database flags. See [supported flags](https://docs.cloud.google.com/sql/docs/mysql/flags#list-flags-mysql) for more information.

## April 06, 2023

Feature

Cascading Replicas is now generally available when migrating from external servers. You can now configure migrated replicas to have read replicas under them before promoting them to primary replica. To learn more, see [External Server Cascading Replicas](https://docs.cloud.google.com/sql/docs/mysql/replication/external-server#es-cascading-replicas).

## March 30, 2023

Feature

Support for [me-central1](https://docs.cloud.google.com/sql/docs/mysql/locations) (Doha) region.

## March 28, 2023

Feature

The changes in the September 15, 2022 Release Notes entry for read replica maintenance are now available. Cloud SQL read replicas follow the [maintenance settings](https://docs.cloud.google.com/sql/docs/mysql/maintenance#management) for the primary instance, including the maintenance window, rescheduling, and the deny maintenance period. During the maintenance event, Cloud SQL maintains the replicas before maintaining the primary instance. For more information, see [How does maintenance affect read replicas?](https://docs.cloud.google.com/sql/docs/mysql/maintenance#read-replicas)

## March 23, 2023

Feature

Support for [europe-west12](https://docs.cloud.google.com/sql/docs/mysql/locations) (Turin) region.

Feature

Cloud SQL for MySQL now supports minor version 8.0.32. To upgrade your existing instance to the new version, see [Upgrade the database minor version](https://docs.cloud.google.com/sql/docs/mysql/upgrade-minor-db-version).

## March 21, 2023

Change

The changes listed in the [June 10 Release Notes entry](https://docs.cloud.google.com/sql/docs/release-notes#June_10_2022) for faster machine type changes were incorrect for Cloud SQL for MySQL, and only applied to Cloud SQL for PostgreSQL and Cloud SQL for SQL Server.

## March 14, 2023

Feature

Cloud SQL for MySQL now supports 106 new database flags. See [supported flags](https://docs.cloud.google.com/sql/docs/mysql/flags#list-flags-mysql) for more information.

## February 28, 2023

Feature

Cloud SQL now supports the ability to get details for a Cloud SQL user for a database instance using the API or gcloud. To learn more about the new method, see [Cloud SQL Admin API REST Resource](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest#rest-resource:-v1.users).

## February 24, 2023

Feature

The Cloud SQL Proxy Operator is now available in public preview. The Cloud SQL Proxy Operator is an open-source Kubernetes operator that automates connecting workloads in a GKE cluster to Cloud SQL databases. To learn more about the Cloud SQL Proxy Operator, see [About the Cloud SQL Proxy Operator](https://docs.cloud.google.com/sql/docs/sql-proxy#proxy-operator).

## February 08, 2023

Feature

The Cloud SQL Auth proxy is a utility for ensuring secure connections to your Cloud SQL instances. The v2 release offers improvements in performance, stability, and telemetry. Among the new features, there's support for:

  * Metrics and tracing with [Cloud Monitoring](https://docs.cloud.google.com/monitoring) and [Cloud Trace](https://docs.cloud.google.com/trace)
  * Support for [Prometheus](https://prometheus.io/)
  * Service account impersonation
  * Separate Dialer functionality released as the [Cloud SQL Go Connector](https://github.com/GoogleCloudPlatform/cloud-sql-go-connector)
  * Configuration with environment variables
  * Fully POSIX-compliant flags



We recommend all customers upgrade to v2 and have released a [migration guide](https://github.com/GoogleCloudPlatform/cloud-sql-proxy/blob/main/migration-guide.md). For more information, see [Cloud SQL Auth proxy](https://github.com/GoogleCloudPlatform/cloud-sql-proxy#readme).

## February 02, 2023

Feature

Cloud SQL supports the preview version of the [Underprovisioned instance recommender](https://docs.cloud.google.com/sql/docs/mysql/recommender-underprovisioned). This service helps you avoid bottlenecks from high CPU and memory usage and minimize the likelihood of out-of-memory events. It gives you recommendations to resize your instances to a machine tier that better suits your workload.

## January 19, 2023

Deprecated

MySQL 8.0.29 was deprecated on January 19, 2023. You will not be able to create new instances for MySQL 8.0.29, upgrade existing instances to MySQL 8.0.29, or promote an existing MySQL 8.0.29 replica to primary. For more information, see [Changes in MySQL 8.0.29](https://dev.mysql.com/doc/relnotes/mysql/8.0/en/news-8-0-29.html).

If you have a MySQL 8.0.29 instance, it will automatically be upgraded to MySQL 8.0.30 as part of regular maintenance prior to March 31, 2023. You can also upgrade your instance to higher available versions. See [Upgrade the database minor version](https://docs.cloud.google.com/sql/docs/mysql/upgrade-minor-db-version) for more information.

## January 18, 2023

Feature

Cloud SQL now supports [viewing an audit log for an automated backup of an instance](https://docs.cloud.google.com/sql/docs/mysql/backup-recovery/view-audit-logs-for-automated-backups) to verify whether the backup is completed successfully. You can also configure a log-based alert so that a user can be notified of the backup's status.

## January 17, 2023

Feature

Cloud SQL for MySQL now supports using the `lower_case_table_names` flag for MySQL 8.0. For more information, see [Configure database flags](https://docs.cloud.google.com/sql/docs/mysql/flags).

## December 27, 2022

Change

The changes listed in the [December 20 release notes entry](https://docs.cloud.google.com/sql/docs/mysql/release-notes#December_20_2022) for the `lower_case_table_names` flag for MySQL 8.0 have been postponed.

## December 21, 2022

Feature

Cloud SQL for MySQL now supports minor version 8.0.31. To upgrade your existing instance to the new version, see [Upgrade the database minor version](https://docs.cloud.google.com/sql/docs/mysql/upgrade-minor-db-version).

## December 20, 2022

Feature

Cloud SQL for MySQL now supports using the `lower_case_table_names` flag for MySQL 8.0. For more information, see [Configure database flags](https://docs.cloud.google.com/sql/docs/mysql/flags).

## December 16, 2022

Feature

Automatic IAM database authentication for Cloud SQL for MySQL is now available. To get started using automatic IAM database authentication, see [Cloud SQL IAM database authentication](https://docs.cloud.google.com/sql/docs/mysql/authentication).

Feature

MySQL 5.7.38 has been upgraded to 5.7.39. For more information, see [MySQL 5.7 release notes](https://dev.mysql.com/doc/relnotes/mysql/5.7/en/).

## December 15, 2022

Feature

You can now allow other Google Cloud services, such as BigQuery, to access data in Cloud SQL for MySQL and make queries against this data over a private connection. For more information, see [Create instances](https://docs.cloud.google.com/sql/docs/mysql/create-instance).

## October 28, 2022

Change

The changes listed in the [September 15 Release Notes entry](https://docs.cloud.google.com/sql/docs/release-notes#September_15_2022) for read replica maintenance have been postponed.

## October 11, 2022

Feature

Cloud SQL supports the preview version of the following recommenders that help you optimize your instance's performance:

  * [High number of open tables recommender](https://docs.cloud.google.com/sql/docs/mysql/recommender-high-number-of-open-tables): Optimize the performance of your instance by increasing the size of table open cache for the Cloud SQL instances that have the number of open tables equal to the table open cache and keep opening too many tables concurrently
  * [High number of tables recommender](https://docs.cloud.google.com/sql/docs/mysql/recommender-high-number-of-tables): Optimize the performance of your instance by reducing the number of tables for the Cloud SQL instances whose table count is too high and close to the SLA limit.



## October 04, 2022

Feature

Terraform is supported when you use [self-service maintenance](https://docs.cloud.google.com/sql/docs/mysql/self-service-maintenance#update-maintenance-version).

## September 29, 2022

Announcement

Cloud SQL for MySQL now supports high-availability for self-service migration. Before starting replication, check the outgoing IP addresses of the Cloud SQL instance and make sure that the appropriate IP addresses are allowlisted on the external source. For more information, see [Start replication on the Cloud SQL instance](https://docs.cloud.google.com/sql/docs/mysql/replication/custom-import-replication-from-external#start_replication_on_the_instance).

Feature

Query insights is now generally available. Query insights helps you detect, diagnose, and prevent query performance problems for Cloud SQL databases. It provides self-service, intuitive monitoring, and diagnostic information that goes beyond detection to help you to identify the root cause of performance problems. To learn more, see [Use Query insights to improve query performance](https://docs.cloud.google.com/sql/docs/mysql/using-query-insights).

## September 21, 2022

Feature

Cloud SQL allows the re-use of an instance name immediately after the instance is deleted. For more information, see the [Cloud SQL for MySQL FAQ](https://docs.cloud.google.com/sql/docs/mysql/faq#reuse).

## September 15, 2022

Feature

Cloud SQL read replicas now follow the [maintenance settings](https://docs.cloud.google.com/sql/docs/mysql/maintenance#management) for the primary instance, including the maintenance window, rescheduling, and the deny maintenance period. During the maintenance event, Cloud SQL maintains the replicas before maintaining the primary instance. For more information, see [How does maintenance affect read replicas?](https://docs.cloud.google.com/sql/docs/mysql/maintenance#read-replicas)

## September 13, 2022

Feature

Support for me-west1 (Tel Aviv).

Feature

MySQL 5.7.37 has been upgraded to 5.7.38. For more information, see [MySQL 5.7 release notes](https://dev.mysql.com/doc/relnotes/mysql/5.7/en/).

## September 12, 2022

Feature

[Cascading Replicas](https://docs.cloud.google.com/sql/docs/postgres/replication#cascading-replicas) is now generally available for Cloud SQL. Customers can now configure PostgreSQL and MySQL for Cloud SQL read replicas to have read replicas under them.

Feature

The In-place Major Version Upgrade feature is now [generally available](https://docs.cloud.google.com/sql/docs/mysql/upgrade-major-db-version-inplace) for Cloud SQL for MySQL.

## September 06, 2022

Feature

Cloud SQL for MySQL now supports minor version 8.0.30. To upgrade your existing instance to the new version, see [Upgrade the database minor version](https://docs.cloud.google.com/sql/docs/mysql/upgrade-minor-db-version).

## August 15, 2022

Feature

By enabling instance deletion protection, you can prevent the accidental removal of Cloud SQL instances. This functionality is generally available.

For more information, see [Prevent deletion of an instance](https://docs.cloud.google.com/sql/docs/mysql/deletion-protection).

## July 14, 2022

Feature

For enhanced security with built-in authentication, Cloud SQL now lets you set [password policies](https://docs.cloud.google.com/sql/docs/mysql/built-in-authentication) at the instance and user levels.

## July 11, 2022

Feature

You can enable [high availability](https://docs.cloud.google.com/sql/docs/mysql/configure-ha#ha-existing) for read replicas. See [Disaster recovery](https://docs.cloud.google.com/sql/docs/mysql/replication/cross-region-replicas#disaster_recovery) for additional information about the use of high-availability replicas in a disaster recovery configuration.

Feature

You can create [external server replicas with HA](https://docs.cloud.google.com/sql/docs/mysql/replication/configure-replication-from-external#setup-replica-instance) enabled.

## July 07, 2022

Feature

Cloud SQL for MySQL now supports setting timezone names as values for the `time_zone` parameter. Refer to the [Cloud SQL documentation](https://docs.cloud.google.com/sql/docs/mysql/flags#timezone-names) for a list of supported timezone names.

## June 28, 2022

Feature

A second June maintenance changelog is now available. For more information, use the links at [Maintenance changelog](https://docs.cloud.google.com/sql/docs/mysql/maintenance-changelog).

## June 27, 2022

Feature

Cloud SQL for MySQL supports in-place major version upgrades in Preview. You can upgrade your instance's major version to a more recent version. For more information, see [Upgrade the database major version in-place](https://docs.cloud.google.com/sql/docs/mysql/upgrade-major-db-version-inplace).

## June 10, 2022

Feature

Cloud SQL now supports faster machine type changes, with connectivity dropping to less than 60 seconds. For more information, see [Impact of changing instance settings](https://docs.cloud.google.com/sql/docs/mysql/instance-settings#impact).

Feature

MySQL 5.7.36 has been upgraded to 5.7.37.

## June 09, 2022

Feature

The June maintenance changelog is now available. For more information, use the links at [Maintenance changelog](https://docs.cloud.google.com/sql/docs/mysql/maintenance-changelog).

## June 08, 2022

Feature

An addendum to the May maintenance changelog shows additional security patches. For more information, use the links at [Maintenance changelog](https://docs.cloud.google.com/sql/docs/mysql/maintenance-changelog).

## June 07, 2022

Feature

Support for us-south1 (Dallas).

## May 26, 2022

Feature

Cloud SQL for MySQL now supports minor version 8.0.29. To upgrade your existing instance to the new version, see [Upgrade the database minor version](https://docs.cloud.google.com/sql/docs/mysql/upgrade-minor-db-version).

## May 24, 2022

Feature

Support for us-east5 (Columbus).

## May 13, 2022

Feature

New maintenance versions are now available through [self-service maintenance](https://docs.cloud.google.com/sql/docs/mysql/self-service-maintenance). See the [maintenance changelog](https://docs.cloud.google.com/sql/docs/mysql/maintenance-changelog) to learn more about these new maintenance versions.

## May 04, 2022

Feature

Support for europe-west9 (Paris).

## May 02, 2022

Feature

New maintenance versions are now available through [self-service maintenance](https://docs.cloud.google.com/sql/docs/mysql/self-service-maintenance). See the [maintenance changelog](https://docs.cloud.google.com/sql/docs/mysql/maintenance-changelog) to learn more about these new maintenance versions.

## April 29, 2022

Feature

MySQL 8.0 is now the default major database version for Cloud SQL for MySQL.

## April 28, 2022

Feature

The following Cloud SQL recommenders that help you optimize your database costs are now generally available:

  * [Idle database instance recommender](https://docs.cloud.google.com/sql/docs/mysql/recommender-sql-idle): Identifies idle database instances in your project and provides recommendations about the savings that you can make by shutting them down. 

  * [Overprovisioned database instance recommender](https://docs.cloud.google.com/sql/docs/mysql/recommender-sql-overprovisioned): Identifies overprovisioned database instances in your project and provides recommendations about the savings that you can make by rightsizing these instances.




## April 25, 2022

Feature

You can now accept a maintenance update on your instance outside of the normal flow of scheduled maintenance. 

While Cloud SQL schedules maintenance updates once every few months to ensure you have the latest maintenance version, you might want to use [self-service maintenance](https://docs.cloud.google.com/sql/docs/mysql/self-service-maintenance) if:

  * You need an update sooner than your next scheduled maintenance event.
  * You want to catch up to the latest maintenance version after skipping your most recent scheduled maintenance event.
  * You want to gain more control over when maintenance is applied



Feature

Cloud SQL now supports maintenance changelogs. Maintenance changelogs provide information about updates available in new maintenance versions, such as database minor version upgrades and patches for security vulnerabilities. For links to current maintenance changelogs for each major database version, see [Cloud SQL maintenance changelogs](https://docs.cloud.google.com/sql/maintenance-changelog).

## April 20, 2022

Feature

Support for europe-west8 region (Milan).

## April 12, 2022

Feature

Customer-managed encryption key (CMEK) organization policy constraints are now available in [Preview](https://cloud.google.com/products#product-launch-stages).

  * `constraints/gcp.restrictNonCmekServices` allows you to control which resources require the use of CMEK.
  * `constraints/gcp.restrictCmekCryptoKeyProjects` allows you to control the projects from which a Cloud KMS key can be used to validate requests.



You can use both constraints together to enforce the use of CMEK from allowed projects. 

To learn more, see [Customer-managed encryption keys (CMEK) organization policies](https://docs.cloud.google.com/sql/docs/mysql/org-policy/org-policy#customer-managed_encryption_keys_cmek_organization_policies). To add CMEK organization policies now, see [Add Cloud SQL organization policies](https://docs.cloud.google.com/sql/docs/mysql/org-policy/configure-org-policy).

## April 01, 2022

Feature

Cloud SQL for MySQL now supports minor versions 8.0.27 and 8.0.28. To upgrade your existing instance to the new version, see [Upgrade the database minor version](https://docs.cloud.google.com/sql/docs/mysql/upgrade-minor-db-version).

## February 28, 2022

Feature

Cloud SQL for MySQL 8.0.26 is now the default minor version. To upgrade your existing instance to the new version, see [Set the MySQL minor version](https://docs.cloud.google.com/sql/docs/mysql/upgrade-minor-db-version).

## February 23, 2022

Feature

If your primary instance uses a private IP address, you can now select an allocated IP range for [clones](https://docs.cloud.google.com/sql/docs/mysql/clone-instance#cloning-an-instance-with-a-private-ip) and [replicas](https://docs.cloud.google.com/sql/docs/mysql/replication/create-replica#gcloud) created from the instance.

## February 17, 2022

Feature

Cloud SQL now supports the use of tags on instances. Tags are key-value pairs you can apply to your resources, such as a project or a Cloud SQL instance, which are used for fine-grained access control. To learn more, see [Access control with Google Cloud tags](https://docs.cloud.google.com/sql/docs/mysql/tags). To use tags now, see [Attach and manage tags on Cloud SQL instances](https://docs.cloud.google.com/sql/docs/mysql/manage-tags).

## January 31, 2022

Feature

The Key Access Justifications (KAJ) feature is now generally available in Cloud SQL. You can use KAJ as part of [Cloud External Key Manager (EKM)](https://docs.cloud.google.com/kms/docs/ekm). KAJ enables you to view the reason for each Cloud EKM request. Additionally, based on the justification provided, you can automatically approve or deny a request. For related information, see the [Overview](https://docs.cloud.google.com/cloud-provider-access-management/key-access-justifications/docs/overview).

## December 16, 2021

Feature

You can now see the database minor version when viewing information about an instance. See [Database versions and version policies](https://docs.cloud.google.com/sql/docs/sqlserver/db-versions) for a list of the latest supported versions.

Feature

You can now [set](https://docs.cloud.google.com/sql/docs/mysql/upgrade-minor-db-version) or [upgrade](https://docs.cloud.google.com/sql/docs/mysql/upgrade-minor-db-version#upgrade_the_minor_version_of_an_existing_instance) your minor version for Cloud SQL for MySQL 8.0.

Feature

Cloud SQL now supports MySQL 8.0.26. To upgrade your existing instance to the new version, see how to [upgrade your minor version](https://docs.cloud.google.com/sql/docs/mysql/upgrade-minor-db-version).

MySQL 5.7.35 has been upgraded to 5.7.36.

Feature

Cloud SQL for MySQL now supports point-in-time recovery using a timestamp. See [Point-in-time recovery](https://docs.cloud.google.com/sql/docs/mysql/backup-recovery/pitr).

Feature

Cloud SQL for MySQL now supports database auditing. Database auditing lets you track specific user actions in the database, such as table updates, read queries, user privilege grants, and others. To learn more, see [MySQL database auditing](https://docs.cloud.google.com/sql/docs/mysql/db-audit).

## December 09, 2021

Feature

Cloud SQL now limits the rate for backup and restore operations on the data disk. For more information, see [Backup rate limitations](https://docs.cloud.google.com/sql/docs/postgres/backup-recovery/backups#backup_rate_limitations) and [Restore rate limitations](https://docs.cloud.google.com/sql/docs/postgres/backup-recovery/restore#restore_rate_limitations).

## November 16, 2021

Feature

Support for [southamerica-west1](https://docs.cloud.google.com/sql/docs/mysql/locations#location-r) (Santiago) region.

## October 08, 2021

Feature

Access Approval is now GA for Cloud SQL. Access Approval enables you to require explicit approval before Google Support may access your database for support purposes.To learn about access approval, see [Overview of Access Approval](https://docs.cloud.google.com/cloud-provider-access-management/access-approval/docs/overview). To set up access approval now, see the [Access Approval Quickstart](https://docs.cloud.google.com/cloud-provider-access-management/access-approval/docs/quickstart).

## October 04, 2021

Feature

Cloud SQL now supports the ability for you to specify IP CIDR ranges from your VPC network for your Cloud SQL instances allowing you to manage your IP address space better. For more information, see [Allocated IP address ranges](https://docs.cloud.google.com/sql/docs/mysql/private-ip#allocated_ip_address_ranges). To start using this feature now, see [Configuring private IP](https://docs.cloud.google.com/sql/docs/mysql/configure-private-ip#new-private-instance) for a new instance.

## September 28, 2021

Feature

Cloud SQL supports the preview version of two recommenders that help you optimize your database costs:

  * [Idle database instance recommender](https://docs.cloud.google.com/sql/docs/mysql/recommender-sql-idle): Identifies idle database instances in your project and provides recommendations about the savings that you can make by shutting them down. 

  * [Overprovisioned database instance recommender](https://docs.cloud.google.com/sql/docs/mysql/recommender-sql-overprovisioned): Identifies overprovisioned database instances in your project and provides recommendations about the savings that you can make by rightsizing these instances.




Feature

When a database instance is nearly out of storage capacity, it's automatically stopped to prevent the loss of information. For more information, see [Stopping an instance](https://docs.cloud.google.com/sql/docs/mysql/start-stop-restart-instance#stop).

## September 14, 2021

Feature

Cloud SQL for MySQL now supports custom formatting controls for CSVs. For more information on how to select custom characters for field delimiters, quotes, escapes, and other characters in admin exports and imports, see [our documentation](https://docs.cloud.google.com/sql/docs/mysql/import-export/import-export-csv).

## September 10, 2021

Feature

The Cloud SQL [out-of-disk recommender](https://docs.cloud.google.com/sql/docs/mysql/using-ood-recommender) is now generally available. This feature proactively generates recommendations that help you reduce the risk of downtime that might be caused by your instances running out of disk space.

## September 08, 2021

Feature

Cloud SQL for MySQL now allows you to specify `mysqldump` options during migration from external servers. For more information, see [Configuring Cloud SQL to replicate from an external server](https://docs.cloud.google.com/sql/docs/mysql/replication/configure-replication-from-external) and [Using a managed import to set up replication from external databases](https://docs.cloud.google.com/sql/docs/mysql/replication/managed-import-replication-from-external).

## September 02, 2021

Feature

Cloud SQL for MySQL now supports using a custom import to set up replication from large external databases. To use this replication option, see [Configuring Cloud SQL to replicate from an external server](https://docs.cloud.google.com/sql/docs/mysql/replication/configure-replication-from-external) and [Using a custom import to set up replication from large external databases](https://docs.cloud.google.com/sql/docs/mysql/replication/custom-import-replication-from-external).

## August 21, 2021

Feature

Cloud SQL now supports [IAM Conditions](https://docs.cloud.google.com/sql/docs/mysql/project-access-control#iam-conditions). 

You can use IAM Conditions to define and enforce conditional, attribute-based access control for Google Cloud resources, including Cloud SQL instances. See [Overview of IAM Conditions](https://docs.cloud.google.com/iam/docs/conditions-overview) for more information.

## August 17, 2021

Feature

MySQL 5.7.33 has been upgraded to 5.7.34.

## August 09, 2021

Feature

The Cloud SQL Admin API v1 is now generally available. It is and will continue to be compatible with the v1beta4 version. There is no requirement to migrate from v1beta4 to the v1 Admin API.

## August 03, 2021

Feature

Support for [northamerica-northeast2-a,b,c](https://docs.cloud.google.com/sql/docs/mysql/locations#location-r) (Toronto) region.

## July 08, 2021

Feature

IAM database authentication for Cloud SQL for MySQL is now generally available. To get started using IAM database authentication, see [Cloud SQL IAM database authentication](https://docs.cloud.google.com/sql/docs/mysql/authentication).

## June 30, 2021

Feature

Cloud SQL for MySQL now offers stored procedures that you can execute on your instances. You can use stored procedures to add or drop secondary indexes on read replicas. See [Cloud SQL stored procedures](https://docs.cloud.google.com/sql/docs/mysql/stored-procedures).

## June 29, 2021

Feature

Cloud SQL for MySQL now supports the [innodb_flush_log_at_trx_commit flag](https://docs.cloud.google.com/sql/docs/mysql/flags#mysql-i).

Feature

Support for [asia-south2](https://docs.cloud.google.com/sql/docs/mysql/locations#location-r) (Delhi) region.

## June 23, 2021

Feature

The following MySQL minor versions have been upgraded:

  * MySQL 5.6.50 is upgraded to 5.6.51
  * MySQL 5.7.32 is upgraded to 5.7.33



Feature

Cloud SQL storage limits are now increased to support up to 64 TB. See [Cloud SQL storage limits](https://docs.cloud.google.com/sql/docs/quotas#storage_limits) for more information.

## June 21, 2021

Feature

Support for [australia-southeast2](https://docs.cloud.google.com/sql/docs/mysql/locations#location-r) (Melbourne) region.

## June 07, 2021

Feature

Cloud SQL now offers [faster maintenance](https://docs.cloud.google.com/sql/docs/mysql/maintenance#how_long_does_maintenance_take), with connectivity dropping for less than 60 seconds on average.

## June 01, 2021

Feature

Cloud SQL for MySQL now supports the [MySQL flags](https://docs.cloud.google.com/sql/docs/mysql/flags) `expire_logs_days` (for MySQL 5.6 and 5.7) and `binlog_expire_logs_seconds` (for MySQL 8.0). Note that if you enable point-in-time recovery, the expiration period of your binary logs will be determined by the lesser of your [transaction log retention period](https://docs.cloud.google.com/sql/docs/mysql/backup-recovery/backups#retention) and the value of these flags.

## May 19, 2021

Feature

Cloud SQL supports the preview version of the [out-of-disk recommender](https://docs.cloud.google.com/sql/docs/mysql/using-ood-recommender). This feature proactively generates recommendations that help you reduce the risk of downtime that might be caused by your instances running out of disk space. These recommendations can be applied when a Cloud SQL instance is trending towards the storage limit.

## March 24, 2021

Feature

Support for [europe-central2 (Warsaw )](https://docs.cloud.google.com/sql/docs/postgres/locations#location-r).

## March 12, 2021

Feature

Cloud SQL for MySQL now supports the innodb_buffer_pool_size flag. To learn more about how to set this flag, see [buffer pool size](https://docs.cloud.google.com/sql/docs/mysql/flags#mysql-i).

## March 05, 2021

Feature

The following MySQL minor versions have been upgraded:

  * MySQL 5.6.47 is upgraded to 5.6.50
  * MySQL 5.7.25 is upgraded to 5.7.32



Feature

Cloud SQL for MySQL now supports flexible instance configurations. Compared to our predefined machine types, flexible instance configurations offer you the extra freedom to configure your instance with the specific number of vCPUs and GB of RAM that fits your workload. To set up a new instance with a flexible instance configuration, see our documentation [here](https://docs.cloud.google.com/sql/docs/mysql/create-instance#create-2nd-gen).

## February 24, 2021

Change

Cloud SQL now offers faster maintenance, with average connectivity loss lasting 90 seconds or less on average. See more about [maintenance timelines](https://docs.cloud.google.com/sql/docs/mysql/maintenance#how_long_does_maintenance_take).

## February 10, 2021

Feature

The Cloud SQL Admin API v1beta4 is now generally available. The URL for the Admin API will continue to refer to v1beta4 for backward compatibility. To start using the Cloud SQL Admin API now, see [Using the Cloud SQL Admin API](https://docs.cloud.google.com/sql/docs/postgres/admin-api).

## January 13, 2021

Feature

Cloud SQL now exposes the metric `database/memory/total_usage`. This metric provides visibility into the database working set (including buffer cache). You can find this metric in the [Metrics explorer](https://docs.cloud.google.com/monitoring/charts/metrics-explorer) within the Monitoring dashboard. 

For more information about `database/memory/total_usage`, see [Cloud SQL Metrics](https://docs.cloud.google.com/monitoring/api/metrics_gcp#gcp-cloudsql).

## December 17, 2020

Feature

In Cloud SQL for MySQL, [parallel replication](https://docs.cloud.google.com/sql/docs/mysql/replication/manage-replicas#configuring-parallel-replication) is generally available for improving replication performance.

## November 19, 2020

Feature

Cloud SQL for MySQL now supports [retention settings for automated backups](https://docs.cloud.google.com/sql/docs/mysql/backup-recovery/backups#retention). You can configure retention of your automated backups for shorter or longer periods (1 to 365 days). The default setting remains 7 days.

Feature

Cloud SQL for MySQL now supports [retention settings for point-in-time recovery](https://docs.cloud.google.com/sql/docs/mysql/backup-recovery/backups#retention). You have the option of retaining logs, used for point-in-time recovery, for shorter periods (1 to 7 days). The default setting is 7 days.

## October 30, 2020

Feature

In Cloud SQL for MySQL, 80 [supported flags](https://docs.cloud.google.com/sql/docs/mysql/flags#list-flags-mysql) that previously were in beta are now generally available.

## October 21, 2020

Feature

Cloud SQL for MySQL supports [binary logging on read replicas](https://docs.cloud.google.com/sql/docs/mysql/replication#bin-log-replica) for MySQL versions 5.7 and 8.0.

## October 12, 2020

Feature

Cloud SQL now offers "deny maintenance periods". With [deny maintenance periods](https://docs.cloud.google.com/sql/docs/mysql/maintenance#deny), you can prevent automatic maintenance from occurring during a specific time period. For example, the end-of-year holiday season is a time of peak load that requires heightened focus on infrastructure stability for many retail businesses. By setting a deny maintenance period from mid-October to mid-January, these businesses can prevent planned upgrades from Cloud SQL during their busiest time of year.

## September 24, 2020

Feature

MySQL 5.6.42 is upgraded to 5.6.47.

## September 21, 2020

Feature

Cloud SQL has upgraded [Replicating from an external server](https://docs.cloud.google.com/sql/docs/mysql/replication/replication-from-external) to version 1.1. You can now:

  * Replicate from sources where GTID is not enabled.
  * Allow Cloud SQL to copy data directly from an external server to a Cloud SQL replica.
  * Use new APIs that give you greater control to verify replication requirements, retry after making external server configuration changes, and remove the 30-minute limit for successful connectivity to an external server.



## September 15, 2020

Feature

Cloud SQL now offers serverless export. With [serverless export](https://docs.cloud.google.com/sql/docs/mysql/import-export/exporting#standard-offload), Cloud SQL performs the export from a temporary instance. Offloading the export operation allows databases on the primary instance to continue to serve queries and perform other operations at the usual performance rate.

## August 25, 2020

Feature

Cloud SQL for MySQL 8.0 is now generally available. If you have not used MySQL 8.0, familiarize yourself with the [What is new in MySQL 8.0](https://dev.mysql.com/doc/refman/8.0/en/mysql-nutshell.html) and [Changes in MySQL 8.0](https://dev.mysql.com/doc/relnotes/mysql/8.0/en/news-8-0-0.html).

For information about the implementation of MySQL 8.0 on Cloud SQL, see the following topics:

  * [MySQL 8.0 authentication](https://docs.cloud.google.com/sql/docs/mysql/features#mysql8-authentication)
  * [Differences between Cloud SQL and standard MySQL functionality](https://docs.cloud.google.com/sql/docs/mysql/features#differences)
  * [Unsupported Cloud SQL feature in MySQL 8.0 for Cloud SQL](https://sql/docs/mysql/features#unsupported_feature_in_mysql_80_for)



To get started using MySQL 8.0 on Cloud SQL, see [Creating instances](https://docs.cloud.google.com/sql/docs/mysql/create-instance).

## June 23, 2020

Feature

Committed use discounts (CUDs) are now available to purchase for Cloud SQL. CUDs provide discounted prices in exchange for your commitment to use a minimum level of resources for a specified term. With committed use discounts for Cloud SQL, you can earn a deep discount off your cost of use in exchange for committing to continuously use database instances in a particular region for a 1- or 3-year term. See the [documentation](https://docs.cloud.google.com/sql/docs/mysql/cud) for more details.

## June 08, 2020

Feature

Support for [asia-southeast2](https://docs.cloud.google.com/sql/docs/mysql/locations) region (Jakarta).

## May 18, 2020

Feature

MySQL 5.6 minor version is upgraded to 5.6.42. MySQL 5.7 minor version is upgraded to 5.7.25.

## May 04, 2020

Deprecated

As [previously announced](https://docs.cloud.google.com/sql/docs/mysql/release-notes#January_29_2019), Cloud SQL First Generation was deprecated on January 29, 2019. All First Generation instances have been migrated to Second Generation. In the documentation and in the Google Cloud Console, "MySQL Second Generation instances" are now referred to simply as "MySQL instances." For general information about this deprecation, see the existing [deprecation notice](https://docs.cloud.google.com/sql/docs/mysql/deprecation-notice).

## April 20, 2020

Feature

Support for [us-west4](https://docs.cloud.google.com/sql/docs/mysql/locations) region (Las Vegas).

## March 24, 2020

Feature

Cloud SQL now supports 96-core machine types for MySQL, Postgres, and SQL Server instances. For pricing-related information, see the [Pricing page](https://cloud.google.com/sql/pricing).

## March 16, 2020

Feature

Cloud SQL now supports read replicas in a different region than that of the primary instance, providing additional protection against regional outages and improving read performance by making replicas available closer to your application. To get started, see [Cross-region replicas](https://docs.cloud.google.com/sql/docs/mysql/replication/cross-region-replicas). 

Cloud SQL instances using [private IP](https://docs.cloud.google.com/sql/docs/mysql/private-ip) are now accessible across regions, at the regular cross-region network egress cost.

## February 27, 2020

Feature

MySQL 5.6.42 is now generally available in Cloud SQL. To start using MySQL 5.6.42, see [Creating Instances](https://docs.cloud.google.com/sql/docs/mysql/create-instance).

## February 24, 2020

Feature

Support for us-west3 region (Salt Lake City).

## February 06, 2020

Deprecated

First Generation instances no longer can be created. As [previously announced](https://docs.cloud.google.com/sql/docs/mysql/release-notes#January_29_2019), Cloud SQL First Generation was deprecated on January 29, 2019. To improve performance, availability, and storage capacity, Cloud SQL Second Generation has replaced First Generation. For more information, see the existing [deprecation notice](https://docs.cloud.google.com/sql/docs/mysql/deprecation-notice) and, if necessary, the [information about upgrading an instance](https://docs.cloud.google.com/sql/docs/mysql/upgrade-2nd-gen).

## January 24, 2020

Feature

Support for [asia-northeast3](https://docs.cloud.google.com/sql/docs/mysql/locations) region (Seoul).

## December 17, 2019

Feature

Cloud SQL now supports VPC Service Controls, which let you add a service perimeter around the Cloud SQL Admin API and host project for Cloud SQL instances to reduce the risk of data exfiltration. To learn more about using VPC Service Controls with Cloud SQL, see [Configuring VPC Service Controls](https://docs.cloud.google.com/sql/docs/postgres/admin-api/configure-service-controls).

## December 13, 2019

Feature

Connection organization policies for Cloud SQL give you the ability to set policies that control access to and from Cloud SQL instances. To learn more about this feature, see [Connection organization policies](https://docs.cloud.google.com/sql/docs/postgres/connection-org-policy). To use this feature, see [Setting organization policies for Cloud SQL](https://docs.cloud.google.com/sql/docs/postgres/configure-org-policy).

Feature

You can now use Cloud VPN with Cloud SQL. To get started, see [Using a VPN with Cloud SQL](https://docs.cloud.google.com/sql/docs/postgres/configure-private-ip#vpn).

## December 10, 2019

Feature

Cloud SQL now offers notifications for upcoming maintenance. See the [Overview of maintenance on Cloud SQL instances](https://docs.cloud.google.com/sql/docs/sqlserver/maintenance). To find out how to sign up for notifications and check your instances for upcoming maintenance, see [Finding and setting maintenance windows](https://docs.cloud.google.com/sql/docs/sqlserver/set-maintenance-window).

## November 25, 2019

Feature

Cloud SQL now supports Access Transparency. As part of Google's long-term commitment to security and transparency, you can use Access Transparency, which provides you with logs of actions that Google staff have taken when accessing your data. To learn more about Access Transparency, see the [Overview of Access Transparency](https://docs.cloud.google.com/logging/docs/audit/access-transparency-overview#overview).

## November 19, 2019

Feature

Cloud SQL now supports customer-managed encryption keys (CMEK). With CMEK, you can encrypt Cloud SQL instances using a key you manage. To learn more about CMEK, see the [Overview of customer managed encryption keys (CMEK)](https://docs.cloud.google.com/sql/docs/mysql/cmek). To start using CMEK, see [Using customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/sql/docs/mysql/configure-cmek).

## October 18, 2019

Feature

Cloud SQL Second Generation MySQL instances have a new high availability (HA) configuration. The new HA configuration, based on Google's [Regional Disks](https://docs.cloud.google.com/compute/docs/disks#repds), eliminates replication lag and, combined with automatic failover, provides isolation from many types of infrastructure, hardware, and software failures. Regional disks also ensure that all previously committed database transactions are persisted and available after failover, right up to the time of the failure.

The new high availability configuration is the default. You can continue to use the API to create instances with the legacy high availability configuration (using failover replicas) until the [upgrade](https://docs.cloud.google.com/sql/docs/mysql/configure-legacy-ha#update-from-legacy) of existing instances occurs in early 2020. To learn how high availability now works for Second Generation MySQL instances, see the [Overview of the high availability configuration](https://docs.cloud.google.com/sql/docs/mysql/high-availability). To enable high availability on existing instances, or to [create new instances](https://docs.cloud.google.com/sql/docs/mysql/configure-ha#ha-create) with high availability, see [Enabling and disabling high availability on an instance](https://docs.cloud.google.com/sql/docs/mysql/configure-ha#ha-existing).

## June 25, 2019

Feature

This release increases the maximum data storage for instances of MySQL (MySQL Second Generation) and PostgreSQL. The maximum data storage is increased from 10,230 GB to 30,720 GB. For Cloud SQL storage limits, see [Limits](https://docs.cloud.google.com/sql/docs/mysql/quotas#limits). You can limit your automatic storage increases; see [Automatic storage increase limit](https://docs.cloud.google.com/sql/docs/mysql/instance-settings#automatic-storage-increase-limit-2ndgen).

## May 24, 2019

Feature

Cloud SQL now allows you to specify a location for backups, and to restrict data to a single region. To learn about custom backup locations, see [Custom backup locations](https://docs.cloud.google.com/sql/docs/mysql/backup-recovery/backups#custom-backup-location). To learn how to set a custom location for a backup, see [Setting and viewing a custom location for backups](https://docs.cloud.google.com/sql/docs/mysql/backup-recovery/backing-up#locationbackups).

## April 18, 2019

Feature

Support for [asia-northeast2](https://docs.cloud.google.com/sql/docs/mysql/locations) region (Osaka, Japan).

## April 03, 2019

Feature

Support added for 122 MySQL flags and 96 PostgreSQL flags. See [Supported PostgreSQL Flags](https://docs.cloud.google.com/sql/docs/postgres/flags#list-flags-postgres) and [Supported MySQL Flags](https://docs.cloud.google.com/sql/docs/mysql/flags#list-flags-mysql).

## March 11, 2019

Feature

Support for [europe-west6](https://docs.cloud.google.com/sql/docs/mysql/locations) region (Zürich, Switzerland).

## January 29, 2019

Feature

Cloud SQL Second Generation [is replacing](https://docs.cloud.google.com/sql/docs/mysql/deprecation-notice) First Generation. Support for First Generation instances for MySQL is ending March 25th, 2020.

## December 06, 2018

Feature

GA support for [Private IP connectivity](https://docs.cloud.google.com/sql/docs/mysql/private-ip).

## October 01, 2018

Feature

[Upgrade to Second Generation](https://docs.cloud.google.com/sql/docs/mysql/upgrade-2nd-gen) generally available for eligible First Generation MySQL instances.

Feature

Support for [asia-east2 region](https://docs.cloud.google.com/sql/docs/mysql/locations) (Hong Kong).

## September 01, 2018

Feature

Beta support for [private IP](https://docs.cloud.google.com/sql/docs/mysql/private-ip) (private services access) connectivity.

Change

[Proxy version 1.12](https://github.com/GoogleCloudPlatform/cloudsql-proxy/releases/tag/1.12) released.

## July 01, 2018

Feature

Support for [us-west2 region](https://docs.cloud.google.com/sql/docs/mysql/instance-locations) (Los Angeles).

Feature

Support for [replication from an external MySQL server to a Cloud SQL Second Generation replica](https://docs.cloud.google.com/sql/docs/mysql/replication/replication-from-external).

## June 01, 2018

Feature

Support for [europe-north1 region](https://docs.cloud.google.com/sql/docs/mysql/instance-locations) (Finland).

Feature

Support for [rotating SSL certificates](https://docs.cloud.google.com/sql/docs/mysql/configure-ssl-instance#how-rotation-works).

Feature

Support for connecting from [Cloud Functions](https://docs.cloud.google.com/sql/docs/mysql/connect-functions) Beta.

## May 01, 2018

Feature

Support for [asia-southeast1 region](https://docs.cloud.google.com/sql/docs/mysql/instance-locations) (Singapore).

## March 01, 2018

Feature

Support for [europe-west4 region](https://docs.cloud.google.com/sql/docs/mysql/instance-locations) (Netherlands).

## February 01, 2018

Change

[Maximum concurrent connections to App Engine](https://docs.cloud.google.com/sql/docs/mysql/faq#sizeqps) updated from 12 to 60.

## January 01, 2018

Feature

Support for [northamerica-northeast1 region](https://docs.cloud.google.com/sql/docs/mysql/instance-locations) (Montréal).

Change

MySQL 5.6 minor version upgraded to 5.6.36.

## November 01, 2017

Feature

Beta support for [the high availability configuration](https://docs.cloud.google.com/sql/docs/postgres/high-availability) and [replication](https://docs.cloud.google.com/sql/docs/postgres/replication/create-replica) for PostgreSQL instances.

## October 01, 2017

Feature

Support for [asia-south1 region](https://docs.cloud.google.com/sql/docs/mysql/instance-locations) (Mumbai).

Change

[Proxy version 1.11](https://github.com/GoogleCloudPlatform/cloudsql-proxy/releases/tag/1.11) released.

## September 01, 2017

Feature

Support for 64-core [machine types](https://docs.cloud.google.com/sql/docs/mysql/instance-settings#machine-type-2ndgen) for MySQL instances and 64 cores for PostgreSQL instances.

Feature

Support for [southamerica-east1 region](https://docs.cloud.google.com/sql/docs/mysql/instance-locations) (São Paulo).

## August 01, 2017

Feature

Support for [europe-west3 region](https://docs.cloud.google.com/sql/docs/mysql/instance-locations) (Frankfurt).

## June 01, 2017

Feature

Support for [labels](https://docs.cloud.google.com/sql/docs/mysql/label-instance).

Change

[Proxy version 1.10](https://github.com/GoogleCloudPlatform/cloudsql-proxy/releases) released.

Feature

Support for [europe-west2 region](https://docs.cloud.google.com/sql/docs/mysql/instance-locations) (London).

Feature

Support for [australia-southeast1 region](https://docs.cloud.google.com/sql/docs/mysql/instance-locations) (Sydney).

## May 01, 2017

Feature

Support for [us-east4 region](https://docs.cloud.google.com/sql/docs/mysql/instance-locations) (Northern Virginia).

Feature

GA support for Second Generation and PostgreSQL instances in version 157.0.0 of the `gcloud` command-line tool. The `beta` version is no longer required for these instances.

Feature

Support for [us-west1 region](https://docs.cloud.google.com/sql/docs/mysql/instance-locations) (Oregon).

## April 01, 2017

Change

[Proxy version 1.09](https://github.com/GoogleCloudPlatform/cloudsql-proxy/releases) released.

## March 01, 2017

Feature

Support for making MySQL general and slow query log files [available through the Stackdriver Log Viewer](https://docs.cloud.google.com/sql/docs/mysql/flags#tips-general-log).

Feature

Support for 32-core [machine types](https://docs.cloud.google.com/sql/docs/mysql/instance-settings#machine-type-2ndgen) for MySQL instances.

## February 01, 2017

Feature

Support for [Identity and Access Management](https://docs.cloud.google.com/iam) (IAM) [predefined roles](https://docs.cloud.google.com/sql/docs/mysql/project-access-control).

## December 01, 2016

Feature

Support for administration of [users](https://docs.cloud.google.com/sql/docs/mysql/create-manage-users) and [databases](https://docs.cloud.google.com/sql/docs/mysql/create-manage-databases) for Second Generation instances in the Google Cloud Console and the Cloud SQL API.

## November 01, 2016

Feature

Support for [Northeastern Asia Pacific region](https://docs.cloud.google.com/sql/docs/mysql/instance-locations) (`asia-northeast1`).

Change

MySQL 5.7 minor version upgraded to 5.7.14.

## August 01, 2016

Feature

[Cloud SQL Second Generation](https://docs.cloud.google.com/sql/docs/mysql/1st-2nd-gen-differences) General Availability.

  * Up to [16 cores and 104 GB RAM](https://cloud.google.com/sql/pricing#machine-types-pricing).
  * [SSD or HDD storage option](https://docs.cloud.google.com/sql/docs/mysql/instance-settings#storage-type-2ndgen) with optional [automatic storage increase capability](https://docs.cloud.google.com/sql/docs/mysql/instance-settings#automatic-storage-increase-2ndgen).
  * Optional [high availability configuration](https://docs.cloud.google.com/sql/docs/mysql/high-availability) (recommended for all production instances).
  * Configurable [maintenance window](https://docs.cloud.google.com/sql/docs/mysql/instance-settings#maintenance-window-2ndgen) and [maintenance timing](https://docs.cloud.google.com/sql/docs/mysql/instance-settings#maintenance-timing-2ndgen).
  * MySQL compatibility: 
    * MySQL 5.6 (5.6.31) and 5.7 (5.7.11)
    * [InnoDB storage engine](https://dev.mysql.com/doc/refman/5.7/en/innodb-storage-engine.html)
    * [GTID support](https://dev.mysql.com/doc/refman/5.7/en/replication-gtids.html)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
