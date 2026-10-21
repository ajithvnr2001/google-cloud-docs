---
url: https://docs.cloud.google.com/sql/docs/postgres/release-notes/
title: Cloud SQL for PostgreSQL release notes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T02:51:29.695379+00:00
---

# Cloud SQL for PostgreSQL release notes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/postgres/release-notes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ PostgreSQL ](https://docs.cloud.google.com/sql/docs/postgres)
  * [ Resources ](https://docs.cloud.google.com/sql/docs/postgres/resources)



Send feedback 

#  Cloud SQL for PostgreSQL release notes Stay organized with collections  Save and categorize content based on your preferences. 

This page documents production updates to Cloud SQL for PostgreSQL. You can check this page for announcements about new or updated features, bug fixes, known issues, and deprecated functionality. 

You can see the latest product updates for all of Google Cloud on the [ Google Cloud](https://docs.cloud.google.com/release-notes) page, browse and filter all release notes in the [Google Cloud console](https://console.cloud.google.com/release-notes), or programmatically access release notes in [BigQuery](https://console.cloud.google.com/bigquery?p=bigquery-public-data&d=google_cloud_release_notes&t=release_notes&page=table). 

To get the latest product updates delivered to you, add the URL of this page to your [feed reader](https://wikipedia.org/wiki/Comparison_of_feed_aggregators), or add the [feed URL](https://docs.cloud.google.com/feeds/cloud-sql-postgres-release-notes.xml) directly. 

## October 16, 2026

Change

Cloud SQL for PostgreSQL now supports enabling [Managed Connection Pooling](https://docs.cloud.google.com/sql/docs/postgres/managed-connection-pooling) on existing [Private Service Connect](https://docs.cloud.google.com/sql/docs/postgres/about-private-service-connect) instances. Previously, Cloud SQL supported enabling Managed Connection Pooling only on new instances using Private Service Connect.

For more information, see [Managed Connection Pooling overview](https://docs.cloud.google.com/sql/docs/postgres/managed-connection-pooling) and [Configure Managed Connection Pooling](https://docs.cloud.google.com/sql/docs/postgres/configure-mcp).

## October 14, 2026

Issue

When you enable the [Knowledge Catalog (formerly Dataplex Universal Catalog)](https://docs.cloud.google.com/sql/docs/postgres/dataplex-catalog-integration) integration on a Cloud SQL for PostgreSQL instance created before April 18, 2026, the integration defaults to once a day instead of near real-time.

Near real-time updates upon Knowledge Catalog enablement aren't yet available for all existing instances. A new announcement will be published when this feature becomes available.

## October 13, 2026

Feature

[Private Service Connect](https://docs.cloud.google.com/sql/docs/postgres/about-private-service-connect) is now the default private IP connectivity option when you create a Cloud SQL for PostgreSQL instance in a new Google Cloud project. Private Service Connect lets you connect to your instance from multiple Virtual Private Cloud (VPC) networks across different groups, projects, or organizations, and supports automatic endpoint and DNS record provisioning. When you configure private IP for an instance, you can still choose to use private services access or both connectivity options.

For more information, see [Private IP configuration options](https://docs.cloud.google.com/sql/docs/postgres/private-ip) and [Configure Private Service Connect](https://docs.cloud.google.com/sql/docs/postgres/configure-private-service-connect).

## October 09, 2026

Feature

**Note:** Near real-time sync upon Knowledge Catalog (KC) enablement isn't available for existing instances created before April 18, 2026. For more information, see the release note from October 14, 2026. 

When you enable [Knowledge Catalog (formerly Dataplex Universal Catalog)](https://docs.cloud.google.com/sql/docs/postgres/dataplex-catalog-integration) integration on an eligible Cloud SQL for PostgreSQL instance created before April 18, 2026 where the integration is currently turned off, the instance now syncs schema and metadata updates to Knowledge Catalog in near real-time instead of once a day (instances created on or after April 18, 2026 have near real-time sync enabled by default).

This feature is available for instances running PostgreSQL version 14.0 or later on the [new network architecture](https://docs.cloud.google.com/sql/docs/postgres/upgrade-cloud-sql-instance-new-network-architecture#overview). If Knowledge Catalog integration is already enabled on the instance with once-a-day updates, you can [deactivate](https://docs.cloud.google.com/sql/docs/postgres/dataplex-catalog-integration#deactivate-dataplex-catalog) and re-enable the integration to switch to near real-time updates.

For more information, see [Enable the integration of Knowledge Catalog on an existing Cloud SQL instance](https://docs.cloud.google.com/sql/docs/postgres/dataplex-catalog-integration#enable-dataplex-catalog).

## October 06, 2026

Change

Cloud SQL for PostgreSQL now supports up to 129,024 concurrent connections for Private Service Connect enabled instances created on or after September 30, 2026 with 16 or more vCPUs.

For more information, see [Configure Private Service Connect](https://docs.cloud.google.com/sql/docs/postgres/configure-private-service-connect#limitations).

## September 29, 2026

Change

You can use the pgAudit extension to prevent string literals that might indicate sensitive information, such as passwords and secrets, from appearing in your log query results. This release provides minor bug fixes to the previous version.

This pgAudit extension capability is supported on `[PostgreSQL version].R20260712.01_RC31` or later.

For more information, see [Audit for PostgreSQL using pgAudit](https://docs.cloud.google.com/sql/docs/postgres/pg-audit).

## September 28, 2026

Breaking

To improve security, removed the `cloudsql.instances.export` permission from the following roles:

  * Cloud SQL Viewer (`roles/cloudsql.viewer`)
  * Basic Reader (`roles/reader`)
  * Basic Viewer (Legacy) (`roles/viewer`)



To retain export capabilities, assign the Cloud SQL Editor (`roles/cloudsql.editor`) role or update custom roles to include the `cloudsql.instances.export` permission.

For more information, see [Cloud SQL roles](https://docs.cloud.google.com/sql/docs/postgres/iam-roles).

## September 21, 2026

Feature

The [C4 machine series](https://docs.cloud.google.com/sql/docs/postgres/machine-series-overview#c4) is available for Cloud SQL for PostgreSQL Enterprise Plus instances in the following regions:

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

Cloud SQL for PostgreSQL now automatically enables point-in-time recovery (PITR) in a separate, asynchronous operation after disaster recovery (DR) switchover and replica failover operations complete. Because PITR enablement no longer blocks switchover and replica failover, these operations complete faster, helping you reduce your recovery time.

For more information, see [Use advanced disaster recovery (DR)](https://docs.cloud.google.com/sql/docs/postgres/use-advanced-disaster-recovery).

## September 14, 2026

Feature

You can use the [`pg_textsearch`](https://github.com/timescale/pg_textsearch) extension in Cloud SQL for PostgreSQL to perform full-text search using the industry-standard [BM25 (Best Matching 25)](https://en.wikipedia.org/wiki/Okapi_BM25) scoring algorithm for highly accurate relevance scoring.

This extension requires PostgreSQL 17 or later and is supported on PostgreSQL release `R20260712.01_06` or later.

For more information, see [Full-text search using pg_textsearch](https://docs.cloud.google.com/sql/docs/postgres/pg-textsearch).

## September 10, 2026

Breaking

Appending `sqlcommenter` tags using the `sql_commenter_enabled` parameter when executing SQL queries on a Cloud SQL remote MCP server is temporarily disabled.

For more information, see [sqlcommenter tags](https://docs.cloud.google.com/sql/docs/postgres/use-cloudsql-mcp#sqlcommenter).

## September 08, 2026

Feature

[Regional endpoints (REP)](https://docs.cloud.google.com/sql/docs/postgres/admin-api/rep) are now generally available ([GA](https://cloud.google.com/products#product-launch-stages)) for the Cloud SQL for PostgreSQL Admin API.

Regional endpoints let you interact with Cloud SQL for PostgreSQL instances using regionalized URLs (such as `sqladmin.[{region}](https://docs.cloud.google.com/sql/docs/postgres/admin-api/rep#supported_regions).rep.googleapis.com`) rather than through a single global endpoint.

Regional endpoints provide regional frontend and load balancing infrastructure that improves data residency by keeping network traffic within the same region as the instance. This reduces the instance's dependency on global frontend infrastructure.

Regional endpoints have strong regional isolation, so the failure of a load balancer or frontend in one region doesn't affect any other region. Regional service load balancers have a separate, regionally isolated control plane.

Regional endpoints are designed to meet stringent data residency and sovereignty standards, such as ITAR and Assured Workloads Regions, ensuring data in transit remains within the committed region.

Certificate management and TLS termination occurs within each region, on the regional load balancer, so data remains encrypted until it reaches its destination region and stays within that region while being processed there.

## September 04, 2026

Feature

The [C4 machine series](https://docs.cloud.google.com/sql/docs/postgres/machine-series-overview#c4) is now available for Cloud SQL for PostgreSQL Enterprise Plus instances in the following regions:

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

For more information about in-place upgrades and downgrades, see [Upgrade in place](https://docs.cloud.google.com/sql/docs/postgres/upgrade-in-place).

## September 02, 2026

Feature

Cloud SQL supports Workforce Identity Federation authentication. This lets you authenticate to your Cloud SQL instance using identities from an external identity provider such as Microsoft Active Directory or Okta. For more information, see [Workforce Identity Federation authentication](https://docs.cloud.google.com/sql/docs/postgres/workforce-authentication).

## August 31, 2026

Feature

You can use the pgAudit extension to prevent string literals that might indicate sensitive information, such as passwords and secrets, from appearing in your log query results.

This pgAudit extension capability is supported on `[PostgreSQL version].R20260712.01_06` or later.

For more information, see [Audit for PostgreSQL using pgAudit](https://docs.cloud.google.com/sql/docs/postgres/pg-audit).

## August 27, 2026

Change

The rollout of the following extension upgrades is complete:

  * `pg_partman` is upgraded from 5.2.4 to 5.4.3.
  * `pgfincore` is upgraded from 1.3.1 to 1.4.
  * `pgvector` is upgraded from 0.8.1 to 0.8.5.



For more information, see [Configure PostgreSQL extensions](https://docs.cloud.google.com/sql/docs/postgres/extensions).

Feature

Cloud SQL now makes it easier to configure [Private Service Connect](https://docs.cloud.google.com/sql/docs/postgres/about-private-service-connect) for your Cloud SQL instance. When you create an instance that's enabled with Private Service Connect, you can choose to automatically create the service connection policy and endpoint in the VPC network that you want to use with Private Service Connect.

For more information, see [Configure Private Service Connect](https://docs.cloud.google.com/sql/docs/postgres/configure-private-service-connect).

## August 25, 2026

Feature

Use assessments ([Preview](https://cloud.google.com/products/#product-launch-stages)) in [Database Center](https://docs.cloud.google.com/database-center/docs/overview) to assess and test the performance impact of database recommendations before you apply them to your production database fleet.

The assessments workflow performs these operations:

  * Clones your database instance.
  * Runs benchmarking simulation tests on the clone.
  * Compares the baseline performance of the clone against the performance after you apply the recommended configuration changes.



For more information, see [Assessments in Database Center](https://docs.cloud.google.com/sql/docs/postgres/assessments-overview).

## August 11, 2026

Feature

The Cloud SQL remote MCP server now supports specialized endpoint URLs (toolsets) for `/readonly`, `/instance_manage`, and `/query_execution`. Specialized toolset URLs let you restrict the set of exposed MCP tools based on your security and workflow requirements.

For more information, see [Available toolsets](https://docs.cloud.google.com/sql/docs/postgres/use-cloudsql-mcp#available-toolsets).

Feature

You can now use the `create_instance` tool in the Cloud SQL remote MCP server to provision free trial instances for testing and development by setting the `free_trial` parameter to `true`.

For more information, see [Create a free trial instance](https://docs.cloud.google.com/sql/docs/postgres/use-cloudsql-mcp#create-free-trial).

Feature

When executing SQL queries using the `execute_sql` or `execute_sql_readonly` tool, setting the `sql_commenter_enabled` parameter to `true` automatically appends sqlcommenter tags (`mcp.tool`, `mcp.server`, `user.identity`, `mcp.client`) to SQL statements for enhanced database observability.

For more information, see [sqlcommenter tags](https://docs.cloud.google.com/sql/docs/postgres/use-cloudsql-mcp#sqlcommenter).

## August 07, 2026

Change

Newly created instances configured with [high availability (HA)](https://docs.cloud.google.com/sql/docs/postgres/high-availability) now have [Knowledge Catalog (formerly Dataplex Universal Catalog)](https://docs.cloud.google.com/sql/docs/postgres/dataplex-catalog-integration) enabled by default.

Cloud SQL for PostgreSQL instances running on PostgreSQL version 14.0 or later send updates and metadata to Knowledge Catalog in near real-time.

You can either verify enablement or [disable the feature](https://docs.cloud.google.com/sql/docs/postgres/dataplex-catalog-integration#deactivate-dataplex-catalog) using the Google Cloud console.

For more information, see [Near real-time](https://docs.cloud.google.com/sql/docs/postgres/dataplex-catalog-integration#near-real-time).

## August 04, 2026

Feature

[DNS automation](https://docs.cloud.google.com/sql/docs/postgres/configure-dns#dns-auto) is now generally available ([GA](https://cloud.google.com/products#product-launch-stages)) on Cloud SQL instances where Private Service Connect is enabled.

You can use DNS automation to provision and manage per-instance DNS records automatically. On Enterprise Plus edition instances where DNS automation is enabled, you can also enable a global write endpoint DNS that automatically resolves to your current primary instance.

## August 03, 2026

Change

You can change the backup plan for your [Cloud SQL enhanced backups](https://docs.cloud.google.com/sql/docs/postgres/backup-recovery/manage-enhanced-backups) without first removing the existing plan. For more information, see [Change your instance's associated backup plan](https://docs.cloud.google.com/sql/docs/postgres/backup-recovery/manage-enhanced-backups#change-plan).

## July 31, 2026

Change

Starting on August 1, 2026, when you create or clone a Cloud SQL instance enabled with Private Service Connect, or when you enable Private Service Connect for an existing instance, then [connection reconciliation](https://docs.cloud.google.com/vpc/docs/about-controlling-access-published-services#connection-reconciliation) behavior is enabled by default and can't be disabled.

When you remove a project from the list of allowed projects, all existing Private Service Connect connections from the removed project are immediately closed (reconciled). This means that applications using Private Service Connect endpoints in those removed projects can't continue to connect to the Cloud SQL instance using those endpoints.

For more information, see [Allowed Private Service Connect projects](https://docs.cloud.google.com/sql/docs/postgres/about-private-service-connect#allowed-psc-projects).

## July 29, 2026

Feature

Cloud SQL for PostgreSQL now supports significantly faster re-encryption of instances and replicas protected by customer-managed encryption keys (CMEKs), and re-encryption now completes with zero downtime. The steps to re-encrypt your instances and replicas are unchanged, but the operation now re-encrypts the underlying disks in-place, without creating re-encryption backups.

For more information, see [Re-encrypt an existing CMEK-enabled instance or replica](https://docs.cloud.google.com/sql/docs/postgres/configure-cmek#reencrypt).

## July 24, 2026

Feature

Cloud SQL for PostgreSQL now supports logical replication using failover slot which you can use with advanced disaster recovery (DR) switchover and replica failover operations to ensure business continuity.

For more information, see [Advanced disaster recovery (DR) with logical failover slot](https://docs.cloud.google.com/sql/docs/postgres/advanced-dr-logical-failover-slot).

## July 20, 2026

Feature

Cloud SQL for PostgreSQL now supports authentication via Secret Manager when executing SQL statements using the Data API (`executeSql`). You can store your database password in a regional secret in Secret Manager and pass the secret version resource name in your API request.

For more information, see [Execute SQL statements on a Cloud SQL instance](https://docs.cloud.google.com/sql/docs/postgres/executesql-instance#configure-db-user).

## June 24, 2026

Change

Cloud SQL now supports Private Service Connect outbound connectivity on the following additional types of instances:

  * Read replica instances.

  * Instances that use advanced disaster recovery features such as switchover and failover operations.




For more information about Private Service Connect outbound connectivity see [About Private Service Connect](https://docs.cloud.google.com/sql/docs/postgres/about-private-service-connect#psc-outbound).

## June 22, 2026

Feature

Customer-managed encryption key (CMEK) support for Cloud SQL enhanced backups is generally available. You can protect your CMEK-enabled Cloud SQL instances using Google Cloud Backup and DR Service.

For more information, see [Choose your backup option](https://docs.cloud.google.com/sql/docs/postgres/backup-recovery/backup-options).

## June 18, 2026

Feature

Cloud SQL is integrated with [Google AI Studio](https://ai.google.dev/aistudio) to help you build full-stack applications that use a [Cloud SQL for PostgreSQL developer edition](https://docs.cloud.google.com/sql/docs/postgres/ai-assisted-coding-and-cloud-sql#cloud-sql-configuration-in-starter-tier) instance as the database. You can enter natural language prompts in the Google AI Studio to build applications backed by Cloud SQL and add features such as authentication, search, and persistent data storage.

For more information, see [Build vibe-coded applications using Google AI Studio and Cloud SQL](https://docs.cloud.google.com/sql/docs/postgres/ai-assisted-coding-and-cloud-sql).

This feature is generally available ([GA](https://cloud.google.com/products#product-launch-stages)).

Feature

The rollout of the following Cloud SQL for PostgreSQL minor version and extension upgrades is complete:

**Minor versions**

  * 14.22 is upgraded to 14.23.
  * 15.17 is upgraded to 15.18.
  * 16.13 is upgraded to 16.14.
  * 17.9 is upgraded to 17.10.
  * 18.3 is upgraded to 18.4.



The new maintenance version is [`[PostgreSQL version].R20260319.07_04`](https://docs.cloud.google.com/sql/docs/postgres/maintenance-changelog). To apply the new maintenance version, see [Perform self-service maintenance](https://docs.cloud.google.com/sql/docs/postgres/self-service-maintenance).

## June 16, 2026

Feature

QueryData adds support for parameterized secure views (PSVs) to help secure applications that use natural language queries. For more information, see [Secure and control access to application data](https://docs.cloud.google.com/sql/docs/postgres/secure-app-data-parameterized-secure-views-qd).

This feature is in [Preview](https://cloud.google.com/products#product-launch-stages).

## June 15, 2026

Feature

You can publish a [Cloud SQL for PostgreSQL conversational analytics agent in Gemini Enterprise](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics/sql-postgres/create-data-agents#publish-agent-gemini-enterprise). This feature is in [Preview](https://cloud.google.com/products/#product-launch-stages).

## June 12, 2026

Feature

You can now create and query [parameterized secure views](https://docs.cloud.google.com/sql/docs/postgres/parameterized-secure-views) in Cloud SQL for PostgreSQL.

Parameterized secure views let you use PostgreSQL views with more granular access control over your data. While you can issue a `GRANT` statement to control whether a user can query a PostgreSQL view, a `GRANT` statement doesn't let you control the data that the view returns based on the user who is making the query.

To gain this level of control, use parameterized secure views. You can define parameters such as a user ID or region within the view. When your application queries the view, a user can provide values for these parameters, which customizes the query results. Using parameterized secure views lets you enforce "least privilege" access to help ensure that your users interact only with the data that is relevant and authorized to them.

This feature is in [Preview](https://cloud.google.com/products#product-launch-stages).

## June 08, 2026

Change

Cloud SQL Enterprise Plus Arm-based C4A machine types, powered by Google's Axion processors, are available in 8 additional regions:

  * `asia-northeast1`: Tokyo, Japan
  * `australia-southeast2`: Melbourne, Australia
  * `europe-north1`: Finland
  * `northamerica-northeast1`: Montréal, Québec, Canada
  * `northamerica-northeast2`: Toronto, Ontario, Canada
  * `southamerica-west1`: Santiago, Chile
  * `us-east5`: Columbus, Ohio, USA
  * `us-west2`: Los Angeles, California, USA



For information about C4A machine types, see [The C4A machine series](https://docs.cloud.google.com/sql/docs/postgres/machine-series-overview#c4a).

## May 12, 2026

Change

The command for upgrading Cloud SQL instances to the new network architecture has been re-enabled.

For more information, see [Upgrade an instance to the new network architecture](https://docs.cloud.google.com/sql/docs/postgres/upgrade-cloud-sql-instance-new-network-architecture).

## May 11, 2026

Feature

Cloud SQL for PostgreSQL now supports regional endpoints for the Cloud SQL Admin API. This feature lets you direct your API calls to a region-specific endpoint. Using a regional endpoint enhances data locality and helps meet strict compliance expectations.

This feature includes: * **Regional boundary restrictions** : Cloud SQL regional endpoints enforce strict matching. The region of the target API resource must match the region of the endpoint exactly. Otherwise, the request is rejected with a 4xx error. * **Restricted API visibility** : When you use a regional endpoint, the Instance.List API only returns resources located within that specific region.

For more information, see [Cloud SQL regional endpoints](https://docs.cloud.google.com/sql/docs/postgres/admin-api/rep).

This feature is in [Preview](https://cloud.google.com/products/#product-launch-stages).

## April 30, 2026

Fixed

Cloud SQL has made the following enhancements to expand the list of eligible Cloud SQL Enterprise Plus edition instances that support planned operations with [near-zero downtime](https://docs.cloud.google.com/sql/docs/postgres/availability#near-zero-downtime).

  * Instances with [connector enforcement enabled](https://docs.cloud.google.com/sql/docs/postgres/connect-connectors#enforce) are eligible for planned operations with near-zero downtime.
  * Instances that use [private services access](https://docs.cloud.google.com/sql/docs/postgres/configure-private-services-access) with a non-RFC 1918 IP address are eligible for planned operations with near-zero downtime.



## April 23, 2026

Feature

The `cloudsql_session_read_only` session parameter provides a robust, non-circumventable mechanism in Cloud SQL for PostgreSQL for preventing data modification during a session. You can use this flag to either make a session temporarily read-only, or make a session permanently, irreversibly read-only.

For more information, see [Create a read-only session in Cloud SQL for PostgreSQL](https://docs.cloud.google.com/sql/docs/postgres/read-only-sessions).

Fixed

Removed a [query insights](https://docs.cloud.google.com/sql/docs/postgres/using-query-insights) limitation for Cloud SQL Enterprise Plus edition and Cloud SQL Enterprise edition instances that use PostgreSQL 18.

Instances using PostgreSQL maintenance version `20260319.00_RC02` or any later version now store application tags when using query insights even if a query has comment tags before the start of a SQL statement.

## April 22, 2026

Feature

[Database Migration Service quick-start migrations](https://docs.cloud.google.com/sql/docs/postgres/quick-start-migrations-guide) are now integrated into Cloud SQL for PostgreSQL to provide a lightweight, continuous migration flow. This feature automates setup for sources with private IPs in a VPC network, including Cloud SQL for PostgreSQL instances and self-managed databases on Compute Engine.

For more information, see [Quick-start migrations overview](https://docs.cloud.google.com/database-migration/docs/about-quick-start-migrations) in the Database Migration Service documentation. This feature is in [Preview](https://cloud.google.com/products#product-launch-stages).

## April 20, 2026

Feature

You can use the [Database Insights remote MCP server](https://docs.cloud.google.com/sql/docs/postgres/reference/mcp/databaseinsights/mcp) to analyze Cloud SQL for PostgreSQL's performance and system metrics. This feature is in [GA](https://cloud.google.com/products/#product-launch-stages).

## April 18, 2026

Feature

Newly created Cloud SQL instances are integrating with Knowledge Catalog (formerly Dataplex Universal Catalog) for data discovery. Instances on PostgreSQL version 14.0 or later will have updates sent to Knowledge Catalog in near real-time. As part of this automatic enablement, we will send metadata to Knowledge Catalog. You can verify if your instance is enabled for integration with Knowledge Catalog by looking at the configuration pane in the Knowledge Catalog console. If you don't want your instance to be integrated with Knowledge Catalog, you can [turn off this feature](https://docs.cloud.google.com/sql/docs/postgres/dataplex-catalog-integration#deactivate-dataplex-catalog).

For more information, see [Near real-time](https://docs.cloud.google.com/sql/docs/postgres/dataplex-catalog-integration#near-real-time).

## April 16, 2026

Feature

The [Cloud SQL remote MCP server](https://docs.cloud.google.com/sql/docs/postgres/use-cloudsql-mcp) is generally available ([GA](https://cloud.google.com/products#product-launch-stages)). The Cloud SQL remote MCP server lets you interact easily with Cloud SQL instances from LLMs, AI applications, and AI-enabled development platforms.

Feature

You can use [DNS automation](https://docs.cloud.google.com/sql/docs/postgres/about-private-service-connect#dns-automation) on Cloud SQL instances where Private Service Connect is enabled to provision and manage per-instance DNS records automatically. On Enterprise Plus edition instances where DNS automation is enabled, you can also enable a global write endpoint DNS that automatically resolves to your current primary instance.

This feature is in [Preview](https://docs.cloud.google.com/products#product-launch-stages).

## April 14, 2026

Breaking

As of April 10, 2026, you can create, run, and edit [Gemini Cloud Assist investigations](https://docs.cloud.google.com/cloud-assist/investigations) only if you have a [Premium Support contract](https://cloud.google.com/support/premium). You can use Gemini Cloud Assist investigations to [monitor and troubleshoot your Cloud SQL instance with AI assistance](https://docs.cloud.google.com/sql/docs/postgres/monitor-troubleshoot-with-ai).

If you ran an investigation prior to April 10, 2026, then the results of the investigation continue to be available to you in the Google Cloud console.

## April 06, 2026

Feature

If the storage capacity of a Cloud SQL instance is larger than your application needs, then you can manually reduce, or shrink, your storage capacity to a smaller size.

Depending on underlying disk size, storage shrink operations might incur considerable downtime. If your instance requires limited downtime, rather than using storage shrink capabilities, we recommend migrating your data to a new, smaller instance using Database Migration Service.

For more information, see [About storage shrink](https://docs.cloud.google.com/sql/docs/postgres/about-storage-shrink).

Feature

The QueryData tool lets you to query the data in your database using conversational language and build data agents. For more information, see [QueryData tool overview](https://docs.cloud.google.com/sql/docs/postgres/data-agent-overview). This feature is available in ([Preview](https://cloud.google.com/products#product-launch-stages)).

The preview release increases the accuracy of SQL generation with value search queries which match values and their context within a database. Value search queries trigger automatically.

## March 30, 2026

Feature

Cloud SQL for PostgreSQL now offers conversational analytics, which lets users query their operational data using natural language. This feature is powered by the [Conversational Analytics API](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/overview), which can help you translate complex human dialog into precise database queries to provide actionable insights. This feature is in [Preview](https://docs.cloud.google.com/products#product-launch-stages). For more information, see [Conversational analytics for Cloud SQL for PostgreSQL overview](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics/sql-postgres).

Breaking

[Vector assist](https://docs.cloud.google.com/sql/docs/postgres/vector-assist-overview) ([Preview](https://docs.cloud.google.com/products#product-launch-stages)) is temporarily disabled for all Cloud SQL for PostgreSQL instances.

## March 17, 2026

Feature

You can now cancel an in-place major version upgrade operation during the main upgrade phase, when the upgrade is actually being performed.

For more information, see [Cancel the major version upgrade](https://docs.cloud.google.com/sql/docs/postgres/upgrade-major-db-version-inplace#cancel-upgrade).

Feature

[Multi-region backup vaults for Cloud SQL enhanced backups](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-vault#multi-regions) are generally available (GA).

This feature lets you store your backup data in multi-region storage locations, providing higher availability and protection against regional outages.

For more information, see [Enhanced backups](https://docs.cloud.google.com/sql/docs/postgres/backup-recovery/backup-options#enhanced-backups).

Feature

Cloud SQL supports cross-project PITR operations for instances protected by backup and DR ([GA](https://cloud.google.com/products/#product-launch-stages)).

This feature lets you restore a Cloud SQL instance to a project other than the project where either the source instance or the backup vault is located.

For more information, see [Perform a cross-project PITR](https://docs.cloud.google.com/sql/docs/postgres/backup-recovery/pitr#perform_a_cross-project_pitr).

## March 13, 2026

Feature

You can now enable automatic server certificate rotation for your Cloud SQL instance. This feature is specifically designed for instances utilizing the Certificate Authority Service (CAS). Automatic server certificate rotation helps you maintain high security standards while removing the operational burden of manual rotation.

For more information about enabling automatic server certificate rotation for your instance, see [Enable automatic server certificate rotation](https://docs.cloud.google.com/sql/docs/postgres/manage-ssl-instance#automatic-server-certificate-rotation-cas).

## March 09, 2026

Feature

You can now execute SQL statements using the [Cloud SQL Data API](https://docs.cloud.google.com/sql/docs/postgres/executesql-instance) for administrative queries.

## February 24, 2026

Feature

It now takes less time to create a Cloud SQL instance when point-in-time recovery (PITR) is enabled, as it is by default in the Google Cloud console. During instance creation, PITR now initially uses an [instant snapshot](https://docs.cloud.google.com/compute/docs/disks/instant-snapshots) instead of a [standard backup](https://docs.cloud.google.com/sql/docs/postgres/backup-recovery/backups#backup-options). and then later converts the snapshot to a standard backup in the background to support [restore operations](https://docs.cloud.google.com/sql/docs/postgres/backup-recovery/restore#tips-pitr).

## February 23, 2026

Feature

Gemini Cloud Assist investigation capabilities are now supported in Cloud SQL for PostgreSQL ([Preview](https://cloud.google.com/products/#product-launch-stages)).

For more information, see [Troubleshoot slow queries with AI assistance](https://docs.cloud.google.com/sql/docs/postgres/troubleshoot-slow-queries).

## February 19, 2026

Feature

Cloud SQL now provides brute-force detection and protection for your Cloud SQL instances. This helps protect your instances from brute-force access attempts by identifying the source and mitigating the risk caused by these attempts. For more information, see [Use brute-force protection](https://docs.cloud.google.com/sql/docs/postgres/use-brute-force-protection).

## February 18, 2026

Change

After March 17, 2026, when you enable the Cloud SQL Admin API (`sqladmin.googleapis.com`)`, the Cloud SQL remote MCP server is enabled automatically.

The Cloud SQL remote MCP server is in [Preview](https://cloud.google.com/products/#product-launch-stages).

Deprecated

Control of MCP use with organization policies is deprecated. After March 17, 2026, organization policies that use the `gcp.managed.allowedMCPServices` constraint won't work, and you can control MCP use with IAM deny policies. For more information about controlling MCP use, see [Control MCP use with IAM](https://docs.cloud.google.com/mcp/control-mcp-use-iam).

## February 17, 2026

Announcement

New best practices are available for securing generative AI agents using Model Context Protocol (MCP) with Google Cloud databases. This guide covers key security measures like least privilege, native database controls, and secure agent design to help you build safer AI applications. For more information, see [Best practices for securing agent interactions with Model Context Protocol](https://docs.cloud.google.com/sql/docs/postgres/secure-agent-interactions-mcp).

## February 09, 2026

Feature

You can now use the [Cloud SQL remote MCP server](https://docs.cloud.google.com/sql/docs/postgres/use-cloudsql-mcp). The Cloud SQL remote MCP server lets you interact easily with Cloud SQL instances from LLMs, AI applications, and AI-enabled development platforms.

This feature is in [Preview](https://cloud.google.com/products/#product-launch-stages).

## February 02, 2026

Feature

You can now update the server certificate authority (CA) mode of an existing Cloud SQL instance. You can update existing instances that use the per-instance CA option (`GOOGLE_MANAGED_INTERNAL_CA`) to use the shared CA option (`GOOGLE_MANAGED_CAS_CA`) or the customer-managed CA option (`CUSTOMER_MANAGED_CAS_CA`).

For more information about the different server CA mode options, see [Certificate authority (CA) hierarchies](https://docs.cloud.google.com/sql/docs/postgres/authorize-ssl#ca-hierarchies).

## January 26, 2026

Feature

You can now assign database roles to built-in database users and IAM database users when you create or update users. For more information about assigning roles, see [built-in database authentication](https://docs.cloud.google.com/sql/docs/postgres/create-manage-users#creating) or [IAM database authentication](https://docs.cloud.google.com/sql/docs/postgres/add-manage-iam-users#add-db-roles).

## January 15, 2026

Feature

Cloud SQL for PostgreSQL now supports fast clone operations within the same zone ([GA](https://cloud.google.com/products#product-launch-stages)).

For more information, see [Clone an instance](https://docs.cloud.google.com/sql/docs/postgres/clone-instance).

## December 17, 2025

Feature

You can build data agents that interact with the data in your database using conversational language. Use these data agents as tools to empower your applications. For more information, see [Data agents overview](https://docs.cloud.google.com/sql/docs/postgres/data-agent-overview). This feature is available in [Preview](https://cloud.google.com/products#product-launch-stages), and access to it requires a [sign-up](https://forms.gle/pJByTWfenZAWbaXo7).

## December 16, 2025

Feature

Cloud SQL enhanced backups are now generally available ([GA](https://cloud.google.com/products#product-launch-stages)).

With enhanced backups, backups are managed and stored in a centralized backup management project that leverages the [Backup and DR service](https://docs.cloud.google.com/backup-disaster-recovery), and provides enforced retention, granular scheduling, and longer retention.

Enhanced backups now also support [point-in-time-recovery (PITR) after instance deletion](https://docs.cloud.google.com/sql/docs/postgres/backup-recovery/restore).

For more information about the available options and their limitations, see [Backup options](https://docs.cloud.google.com/sql/docs/postgres/backup-recovery/backup-options). For more information about enhanced backups pricing, see [Backup and DR pricing](https://cloud.google.com/backup-disaster-recovery/pricing).

## November 20, 2025

Feature

PostgreSQL version 18 is now [generally available](https://cloud.google.com/products#product-launch-stages) for Cloud SQL for PostgreSQL.

You can now use [Database Migration Service](https://docs.cloud.google.com/database-migration/docs) with Cloud SQL for PostgreSQL when using PostgreSQL version 18.

To upgrade your instance to PostgreSQL 18, see [Upgrade the database major version in-place](https://docs.cloud.google.com/sql/docs/postgres/upgrade-major-db-version-inplace).

The following extensions are also now available for PostgreSQL 18:

  * `pg_hint_plan`
  * `pgrouting`
  * `anonymizer`
  * `pg_wait_sampling`
  * `tds_fdw`
  * `plpgsql_check`



For more information about these extensions, see [Configure PostgreSQL extensions](https://docs.cloud.google.com/sql/docs/postgres/extensions).

## November 19, 2025

Feature

Cloud SQL for PostgreSQL now supports Vector assist ([Preview](https://cloud.google.com/products#product-launch-stages)).

Vector assist is a Cloud SQL for PostgreSQL extension that simplifies the deployment and management of your Cloud SQL vector workloads. It helps you set up production-ready vector search capabilities, such as embedding generation, query optimization, and index creation.

For more information about vector assist, how it works, and its limitations, see [Vector assist overview](https://docs.cloud.google.com/sql/docs/postgres/vector-assist-overview).

Feature

The rollout of the following minor version and extension upgrades is complete:

**Minor versions**

  * 13.22 is upgraded to 13.23.
  * 14.19 is upgraded to 14.20.
  * 15.14 is upgraded to 15.15.
  * 16.10 is upgraded to 16.11.
  * 17.6 is upgraded to 17.7.
  * 18 is upgraded to 18.1.



**Extensions**

  * `Pgvector` is upgraded from 0.8.0 to 0.8.1.



To use these versions of the extensions and plugins, update your instance to `[PostgreSQL version].R20251004.01_19`.

If you use a maintenance window, then the updates to the minor, extension, and plugin versions happen according to the timeframe that you set in the window. Otherwise, the updates occur within the next few weeks.

For more information on checking your maintenance version, see [Self-service maintenance](https://docs.cloud.google.com/sql/docs/postgres/self-service-maintenance). To find your maintenance window or to manage maintenance updates, see [Find and set maintenance windows](https://docs.cloud.google.com/sql/docs/postgres/set-maintenance-window).

## November 17, 2025

Feature

Cloud SQL now offers a free trial instance for both existing and new Google Cloud customers. A free trial instance lets you test advanced Cloud SQL capabilities and features for up to 30 days without any financial commitment.

For information about a free trial instance, and its inclusions and conditions, see [Free trial instance overview](https://cloud.google.com/sql/docs/postgres/free-trial-instance).

## November 14, 2025

Feature

Cloud SQL for PostgreSQL now supports [read pool autoscaling](https://docs.cloud.google.com/sql/docs/postgres/read-pool-autoscaling) [(GA)](https://cloud.google.com/products#product-launch-stages), which helps you more easily manage your application's workload needs.

This feature automates read pool scale in and scale out operations based on one or both of the following conditions:

  * Allowed CPU usage of the read pool
  * Allowed number of client connections to the read pool



## November 05, 2025

Feature

The rollout of the following extension versions, plugin versions, and extension support is underway:

**Extensions and plugins**

  * `plpgsql_check` is upgraded from 2.8.1 to 2.8.3 for PostgreSQL versions 14 and later.
  * `pg_wait_sampling` is upgraded from 1.1.6 to 1.1.9 for PostgreSQL versions 13 and later.
  * `tds_fdw` is upgraded from 2.0.4 to 2.0.5.



The following extensions are available for PostgreSQL 18:

  * `anon`
  * `pg_hint_plan`
  * `pg_wait_sampling`
  * `plpgsql_check`
  * `tds_fdw`



To use these versions of the extensions and plugins, update your instance to `[PostgreSQL version].R20251004.01_14`.

If you use a maintenance window, then the updates to the minor, extension, and plugin versions happen according to the timeframe that you set in the window. Otherwise, the updates occur within the next few weeks.

For more information on checking your maintenance version, see [Self-service maintenance](https://docs.cloud.google.com/sql/docs/postgres/self-service-maintenance). To find your maintenance window or to manage maintenance updates, see [Find and set maintenance windows](https://docs.cloud.google.com/sql/docs/postgres/set-maintenance-window).

## October 27, 2025

Feature

The rollout of the following extension versions and plugin versions is underway:

**Extensions and plugins**

  * `pg_squeeze` is upgraded from 1.8 to 1.9 for PostgreSQL version 13 and later.
  * `pg_cron` is upgraded from 1.6.4 to 1.6.7 for PostgreSQL version 10 and later.
  * `postgis` is upgraded from 3.5.2 to 3.6.0 for PostgreSQL version 13 and later.
  * `rdkit` is upgraded from 4.6.1 to 4.7.0.



To use these versions of the extensions and plugins, update your instance to `[PostgreSQL version].R20251004.01_07`.

If you use a maintenance window, then the updates to the minor, extension, and plugin versions happen according to the timeframe that you set in the window. Otherwise, the updates occur within the next few weeks.

For more information on checking your maintenance version, see [Self-service maintenance](https://docs.cloud.google.com/sql/docs/postgres/self-service-maintenance). To find your maintenance window or to manage maintenance updates, see [Find and set maintenance windows](https://docs.cloud.google.com/sql/docs/postgres/set-maintenance-window).

## October 23, 2025

Feature

Cloud SQL now proactively detects and works to cancel high memory usage connections to prevent out-of-memory (OOM) failures. For more information, see [Cancelled queries due to high memory usage](https://cloud.google.com/sql/docs/postgres/manage-memory-usage-best-practices#cancelled-query).

## October 17, 2025

Feature

Cloud SQL Enterprise edition now supports a new machine series called the N4 machine series. This machine series provides balanced price-to-performance and uses the Hyperdisk Balanced storage. You can create custom machine types for the N4 machine series with up to 80 vCPUs and up to 640 GB memory. The N4 machine series is [generally available](https://cloud.google.com/products#product-launch-stages) (GA).

For more information about the N4 machine series and its availability, see [Machine series overview](https://docs.cloud.google.com/sql/docs/postgres/machine-series-overview).

Feature

The [C4A machine series](https://docs.cloud.google.com/sql/docs/postgres/machine-series-overview#c4a) is now [generally available](https://cloud.google.com/products#product-launch-stages) (GA).

The C4A machine series is supported for Cloud SQL Enterprise Plus edition instances, and provides optimized price-performance and delivers predictable high performance for high demand Cloud SQL workloads. It uses the Hyperdisk Balanced storage.

For more information about the C4A machine series and its availability, see [Machine series overview](https://docs.cloud.google.com/sql/docs/postgres/machine-series-overview).

## October 06, 2025

Feature

You can now assess the upgrade readiness of your Cloud SQL for PostgreSQL instances before a major version upgrade by running a precheck. This precheck either confirms your instance can be upgraded, or lists issues and their solutions that need to be fixed prior to upgrading. For more information, see [Assess upgrade readiness for your instance](https://docs.cloud.google.com/sql/docs/postgres/upgrade-major-db-version-inplace#precheck).

## October 03, 2025

Feature

Cloud SQL for PostgreSQL now supports PostgreSQL version 18 in [Preview](https://cloud.google.com/products#product-launch-stages).

PostgreSQL 18 is a newly supported version. We strongly recommend that you review the changes in the release and validate the readiness of your instance thoroughly prior to upgrading your instance to this version.

The following information applies to flags and extensions for PostgreSQL 18:

**Flags**

The following new flags are available for PostgreSQL 18 only:

  * `autovacuum_vacuum_max_threshold`
  * `autovacuum_worker_slots`
  * `enable_distinct_reordering`
  * `enable_self_join_elimitation`
  * `io_max_concurrency`
  * `io_method`
  * `io_workers`
  * `log_lock_failures`
  * `max_active_replecation_origins`
  * `track_cost_delay_timing`
  * `vacuum_max_eager_freeze_failure_rate`
  * `vacuum_truncate`



For more information, see [Configure database flags](https://docs.cloud.google.com/sql/docs/postgres/flags).

**Extensions**

The following extensions aren't available for PostgreSQL 18:

  * `pgRouting`
  * `plpgsql_check`
  * `pg_hint_plan`
  * `pgrouting`
  * `anonymizer`
  * `pg_wait_sampling`
  * `tds_fdw`



For more information, see [Configure PostgreSQL extensions](https://docs.cloud.google.com/sql/docs/postgres/extensions).

To create a new instance using PostgreSQL 18, see [Create instances](https://docs.cloud.google.com/sql/docs/postgres/create-instance).

## September 29, 2025

Feature

You can now [use Gemini's capabilities to fix errors in a query within Cloud SQL Studio](https://cloud.google.com/sql/docs/postgres/write-sql-gemini#fix-query) ([Preview](https://cloud.google.com/products#product-launch-stages)).

## September 25, 2025

Feature

Cloud SQL Managed Connection Pooling is now generally available ([GA](https://cloud.google.com/products#product-launch-stages)). Managed Connection Pooling lets you scale your workloads by optimizing resource utilization for Cloud SQL instances using pooling. You can now also use [IAM authentication](https://docs.cloud.google.com/sql/docs/postgres/iam-authentication) to secure connections when using Managed Connection Pooling. 

For more information, see [Managed Connection Pooling overview](https://docs.cloud.google.com/sql/docs/postgres/managed-connection-pooling).

## September 23, 2025

Feature

You can now provision, manage and query your databases using the dedicated Gemini CLI extension for Cloud SQL for PostgreSQL. The extension provides full lifecycle control of your database—from provisioning instances, to exploring schemas and troubleshooting issues—from your command-line interface. 

For more information, see [Use Cloud SQL for PostgreSQL with MCP, Gemini CLI, and other agents](https://cloud.google.com/sql/docs/postgres/pre-built-tools-with-mcp-toolbox).

Feature

You can now retain point-in-time recovery (PITR) logs for an instance after its deletion for a specified retention period. These logs can be used to restore the deleted instance to a specific point in time. For more information, see [Restore a deleted instance using PITR](https://docs.cloud.google.com/sql/docs/postgres/backup-recovery/restore#deleted-instance).

## September 17, 2025

Feature

The rollout of the following minor version upgrades is complete:

**Minor versions**

  * 13.21 is upgraded to 13.22.
  * 14.18 is upgraded to 14.19.
  * 15.13 is upgraded to 15.14.
  * 16.9 is upgraded to 16.10.
  * 17.5 is upgraded to 17.6.



Cloud SQL for PostgreSQL adds support for the following extensions:

**Extensions**

  * `plpgsql_check 2.8` is available for PostgreSQL version 14 and later.
  * `roaringbitmap 0.5` is available for PostgreSQL version 12 and later.



To use these minor versions and the new extensions, update your instance to `[PostgreSQL version].R20250727.00_23`.

If you use a maintenance window, then the updates to the minor, extension, and plugin versions happen according to the timeframe that you set in the window. Otherwise, the updates occur within the next few weeks.

For more information on checking your maintenance version, see [Self-service maintenance](https://docs.cloud.google.com/sql/docs/postgres/self-service-maintenance). To find your maintenance window or to manage maintenance updates, see [Find and set maintenance windows](https://docs.cloud.google.com/sql/docs/postgres/set-maintenance-window).

## September 12, 2025

Feature

If a specific active query is blocked or running much longer than expected, it can block other dependent queries. Cloud SQL for PostgreSQL offers an optional feature that lets you terminate specific long-running or blocked active queries.

For more information, see [Blocked active queries (Preview)](https://cloud.google.com/sql/docs/postgres/monitor-active-queries#blocked-active-queries).

## September 09, 2025

Feature

The rollout of the following extension versions is complete:

**Extensions and plugins**

  * `pg_ivm` is upgraded from 1.9 to 1.11.
  * `pg_background` is upgraded from 1.2 to 1.3.
  * `google_ml_integration` is upgraded from 1.4.2 to 1.4.3. 



To use these versions of the extensions, update your instance to [`PostgreSQL version].R20250727.00_14`. If you use a maintenance window, then the updates to the minor, extension, and plugin versions happen according to the timeframe that you set in the window. Otherwise, the updates occur within the next few weeks.

For more information on checking your maintenance version, see [Self-service maintenance](https://docs.cloud.google.com/sql/docs/postgres/self-service-maintenance). To find your maintenance window or to manage maintenance updates, see [Find and set maintenance windows](https://docs.cloud.google.com/sql/docs/postgres/set-maintenance-window).

## September 08, 2025

Feature

Cloud SQL read pools are now generally available and provide operational simplicity and scaling for your read workloads.

Read pools provide a single endpoint in front of up to 20 read pool nodes and automatically load balance traffic.

You can scale your read pool in several ways: 

  * **Scale in or out** : scale load balancing capacity horizontally by modifying the number of read pool nodes in the read pool. Each read pool supports up to 20 read pool nodes.
  * **Scale up or down** : scale load balancing capacity vertically by modifying the machine type associated with a read pool node. Once defined, configuration is uniformly applied across each read pool node in the read pool.



For more information, see [About read pools](https://docs.cloud.google.com/sql/docs/postgres/about-read-pools).

Feature

You can have Cloud SQL create a [Private Service Connect](https://docs.cloud.google.com/sql/docs/postgres/about-private-service-connect#psc-endpoint) endpoint automatically. You can use this endpoint to access Cloud SQL instances through a VPC network. For more information, see [Create a Private Service Connect endpoint automatically](https://docs.cloud.google.com/sql/docs/postgres/configure-private-service-connect#create-endpoint-automatically). 

This feature is now generally available ([GA](https://cloud.google.com/products#product-launch-stages)).

## September 04, 2025

Change

The release note on [August 13, 2025](https://docs.cloud.google.com/sql/docs/postgres/release-notes#August_13_2025) regarding Private Service Connect (PSC) outbound connectivity has been updated.

PSC outbound connectivity is required for [homogeneous migrations](https://docs.cloud.google.com/database-migration/docs/homogeneous-migrations) to PSC-enabled Cloud SQL instances using [Database Migration Service](https://docs.cloud.google.com/database-migration/docs). For more information, see [PSC outbound connections](https://docs.cloud.google.com/sql/docs/postgres/about-private-service-connect#psc-outbound).

## September 03, 2025

Feature

You can now enable your instance to take a final backup at instance deletion and define its retention period by setting the final backup [instance setting](https://docs.cloud.google.com/sql/docs/postgres/instance-settings). 

You can also create a [custom organization policy](https://docs.cloud.google.com/sql/docs/postgres/org-policy/custom-org-policy) to define final backup instance settings. For more information, see [Final backup](https://docs.cloud.google.com/sql/docs/postgres/backup-recovery/backups#final-backup).

## August 21, 2025

Feature

You can save and manage SQL queries in Cloud SQL Studio. This feature is in [Preview](https://cloud.google.com/products#product-launch-stages). For more information, see [Saved queries overview](https://docs.cloud.google.com/sql/docs/postgres/saved-queries).

## August 15, 2025

Feature

Now you can use [Private Service Connect backends](https://cloud.google.com/sql/docs/postgres/about-private-service-connect#psc-backend), as an alternative to Private Service Connect endpoints, to access Cloud SQL instances.

Feature

Now you can create an IPv6 endpoint for Private Service Connect (PSC) connections. For more information, see [Connect to an instance using Private Service Connect](https://cloud.google.com/sql/docs/postgres/configure-private-service-connect#create-psc-endpoint).

Deprecated

You can no longer set a deny maintenance period for instances that are running a maintenance version older than 12 months. To update your instance, [perform self-service maintenance](https://docs.cloud.google.com/sql/docs/postgres/self-service-maintenance) or wait until the [next maintenance window](https://docs.cloud.google.com/sql/docs/postgres/set-maintenance-window#find-maintenance-api) to update your instance automatically. For more information about maintenance, see [Maintenance updates on Cloud SQL instances](https://docs.cloud.google.com/sql/docs/postgres/maintenance).

## August 13, 2025

Feature

Cloud SQL now supports Private Service Connect (PSC) outbound connectivity. With PSC outbound connectivity, you can attach a PSC interface to your existing Cloud SQL PSC-enabled instances to allow your instances to make outbound connections to your network. This is required for [homogeneous migrations](https://docs.cloud.google.com/database-migration/docs/homogeneous-migrations) to PSC-enabled Cloud SQL instances using [Database Migration Service](https://docs.cloud.google.com/database-migration/docs). For more information, see [PSC outbound connections](https://docs.cloud.google.com/sql/docs/postgres/about-private-service-connect#psc-outbound).

## August 07, 2025

Change

Cloud SQL for Enterprise Plus edition supports quality enhancements for [AI-assisted troubleshooting](https://cloud.google.com/sql/docs/postgres/observe-troubleshoot-with-ai). With AI-assisted troubleshooting, you can resolve complex database performance issues like [slow queries](https://cloud.google.com/sql/docs/postgres/troubleshoot-slow-queries) and [high load](https://cloud.google.com/sql/docs/postgres/troubleshoot-high-database-load) for your instances in a guided manner. To use AI-assisted troubleshooting, you need [Gemini Cloud Assist](https://cloud.google.com/gemini/docs/cloud-assist/overview) and [query insights](https://cloud.google.com/sql/docs/postgres/using-query-insights#enable-insights) for Enterprise Plus edition.

## August 04, 2025

Issue

PostgreSQL has identified a [bug](https://www.postgresql.org/message-id/flat/680bdaf6-f7d1-4536-b580-05c2760c67c6%40deepbluecap.com) in [PostgreSQL's May 8, 2025 release](https://www.postgresql.org/about/news/postgresql-175-169-1513-1418-and-1321-released-3072/) that is causing logical replication to halt. Cloud SQL for PostgreSQL released `[PostgreSQL version].R20250302.00_19` on [May 22, 2025](https://docs.cloud.google.com/sql/docs/postgres/release-notes#May_22_2025), which is impacted by this bug. 

If you use logical replication with your Cloud SQL for PostgreSQL instances, then we recommend that you don't update your instances to this version or any self-service maintenance version released after May 22, 2025, due to this PostgreSQL bug. We also recommend not performing a [major version upgrade](https://docs.cloud.google.com/sql/docs/postgres/upgrade-major-db-version-inplace) on your instances, since it adopts the latest self-service maintenance version. 

We expect a fix for this issue in the next automatically-scheduled maintenance. For more information about this bug, see [Logical replication 'invalid memory alloc request size 1585837200' after upgrading to 17.5](https://www.postgresql.org/message-id/flat/680bdaf6-f7d1-4536-b580-05c2760c67c6%40deepbluecap.com).

## July 31, 2025

Feature

Cloud SQL now offers two options of backup services to manage your instance's backups:

  * **Enhanced backups** ([Preview](https://cloud.google.com/products#product-launch-stages)): backups are managed and stored in a centralized backup management project that leverages the [Backup and DR service](https://docs.cloud.google.com/backup-disaster-recovery), and provides enforced retention, granular scheduling, and longer retention. 

  * **Standard backups** (existing option): backups are created, managed, and stored in the same project as your Cloud SQL instances. 




You can choose between these options based on your instance's requirements and needs. Although instances can't use both backup options at the same time, Cloud SQL gives you the ability to switch between these backup options as necessary. 

For more information about the available options and their limitations, see [Backup options](https://docs.cloud.google.com/sql/docs/postgres/backup-recovery/backups#backup-options).

## July 02, 2025

Feature

The write endpoint feature for Cloud SQL Enterprise Plus edition instances is now [generally available](https://cloud.google.com/products#product-launch-stages) (GA). This endpoint is a global domain name service (DNS) name and resolves to the IP address of the current primary Cloud SQL instance that's enabled with private services access.

By using a write endpoint, you can avoid having to make application connection changes after performing a switchover or replica failover operation to test or mitigate a region failure.

For more information, see [Connect to an instance using a write endpoint](https://docs.cloud.google.com/sql/docs/postgres/connect-to-instance-using-write-endpoint).

## May 22, 2025

Feature

The rollout of the following minor versions, extension versions, and plugin versions is complete:

**Minor versions**

  * 13.20 is upgraded to 13.21.
  * 14.17 is upgraded to 14.18.
  * 15.12 is upgraded to 15.13.
  * 16.8 is upgraded to 16.9.
  * 17.4 is upgraded to 17.5.



**Extensions and plugins**

  * pg_squeeze is upgraded from 1.5 to 1.8 for all PostgreSQL versions 12 and above.



To use these versions of the extensions, update your instance to `[PostgreSQL version].R20250302.00_19`.

If you use a maintenance window, then the updates to the minor, extension, and plugin versions happen according to the timeframe that you set in the window. Otherwise, the updates occur within the next few weeks. 

For more information on checking your maintenance version, see [Self-service maintenance](https://docs.cloud.google.com/sql/docs/postgres/self-service-maintenance). To find your maintenance window or to manage maintenance updates, see [Find and set maintenance windows](https://docs.cloud.google.com/sql/docs/postgres/set-maintenance-window).

Feature

You can now create an instance with both private services access and Private Service Connect enabled. You can also enable Private Service Connect on an existing private services access instance. This feature is now generally available ([GA](https://cloud.google.com/products#product-launch-stages)).

For more information, see [Configure both private services access and Private Service Connect](https://docs.cloud.google.com/sql/docs/postgres/configure-private-services-access-and-private-service-connect).

## May 15, 2025

Feature

You can now use [advanced disaster recovery (DR)](https://docs.cloud.google.com/sql/docs/postgres/intro-to-cloud-sql-disaster-recovery#advanced-dr) for your Private Service Connect (PSC) enabled Cloud SQL Enterprise Plus edition instances. With advanced DR, you can:

  * Designate a cross-region disaster recovery (DR) replica
  * Perform a cross-region replica failover for disaster recovery
  * Restore your original deployment by using zero-data loss switchover



You can also use switchover to simulate disaster recovery without data loss. For more information, see [Use advanced disaster recovery (DR)](https://docs.cloud.google.com/sql/docs/postgres/use-advanced-disaster-recovery). This feature is [generally available](https://cloud.google.com/products#product-launch-stages) (GA).

## May 08, 2025

Change

If you create an instance using the Google Cloud Console, then the per-instance CA (`GOOGLE_MANAGED_INTERNAL_CA`) option is now the default [server certificate authority (CA) mode](https://docs.cloud.google.com/sql/docs/postgres/authorize-ssl#ca-hierarchies) for your Cloud SQL instance.

For users of the [Cloud SQL Auth Proxy](https://docs.cloud.google.com/sql/docs/postgres/sql-proxy): 

  * If the Cloud SQL instance to which you're connecting is using [shared certificate authority (CA)](https://docs.cloud.google.com/sql/docs/postgres/authorize-ssl#shared-regional-ca) for its `serverCaMode` setting, then on the client side, you must use Cloud SQL Auth Proxy version 2.13.0 or later.
  * If the Cloud SQL instance to which you're connecting is using [customer-managed CA](https://docs.cloud.google.com/sql/docs/postgres/authorize-ssl#customer-managed-ca) for its `serverCaMode` setting, then on the client side, you must use Cloud SQL Auth Proxy version 2.14.3 or later.



## May 07, 2025

Feature

You can migrate to AlloyDB for PostgreSQL using your Cloud SQL for PostgreSQL backup ([GA](https://cloud.google.com/products#product-launch-stages)). The Google Cloud CLI is also supported. For more information, see [Migrate from Cloud SQL for PostgreSQL to AlloyDB](https://docs.cloud.google.com/sql/docs/postgres/backup-recovery/migrate-cloud-sql-to-alloydb).

## May 02, 2025

Feature

You can now [set up custom DNS names by configuring the custom subject alternative name (SAN)](https://docs.cloud.google.com/sql/docs/postgres/custom-dns-name) for your instance. After you set up DNS name resolution, you can connect to your Cloud SQL instance using the custom DNS name instead of using an IP address. This feature is available only for instances that are configured with the [customer-managed certificate authority (CA)](https://docs.cloud.google.com/sql/docs/postgres/customer-managed-ca) (`CUSTOMER_MANAGED_CAS_CA`) option as its server CA mode. 

Custom SAN configuration for instances is [generally available](https://cloud.google.com/products#product-launch-stages) (GA).

## May 01, 2025

Feature

Cloud SQL gives you the flexibility to choose between three [CA hierarchy options](https://docs.cloud.google.com/sql/docs/postgres/authorize-ssl#ca-hierarchies) when you [create a Cloud SQL instance](https://docs.cloud.google.com/sql/docs/postgres/create-instance).

You can choose between the per-instance CA (`GOOGLE_MANAGED_INTERNAL_CA`), the shared CA (`GOOGLE_MANAGED_CAS_CA`), or the customer-managed CA (`CUSTOMER_MANAGED_CAS_CA`) options as the server certificate authority (CA) mode for your instance. If you create an instance using the Google Cloud Console, then the shared CA option, (`GOOGLE_MANAGED_CAS_CA`), is the default configuration. If you create an instance using gcloud, the Cloud SQL Admin REST API, or Terraform, then the per-instance CA option (`GOOGLE_MANAGED_INTERNAL_CA`) is the default configuration.

The shared CA and customer-managed CA options are now [generally available](https://cloud.google.com/products#product-launch-stages) (GA).

## April 30, 2025

Feature

The rollout of the following extension versions and plugin versions is complete:

**Extensions and plugins**

  * `pg_partman` is upgraded from 5.0.1 to 5.2.4 (for PostgreSQL versions 14 and later).



To use this version of the extension, update your instance to `[PostgreSQL version].R20250302.00_10`.

If you use a maintenance window, then the updates to the minor, extension, and plugin versions happen according to the timeframe that you set in the window. Otherwise, the updates occur within the next few weeks.

For more information on checking your maintenance version, see [Self-service maintenance](https://docs.cloud.google.com/sql/docs/postgres/self-service-maintenance). To find your maintenance window or to manage maintenance updates, see [Find and set maintenance windows](https://docs.cloud.google.com/sql/docs/postgres/set-maintenance-window).

## April 24, 2025

Feature

[Private Service Connect endpoint propagation](https://docs.cloud.google.com/sql/docs/postgres/about-private-service-connect#psc-endpoint-propagation) is now [generally available](https://cloud.google.com/products#product-launch-stages) (GA). You can use the Network Connectivity Center hub to propagate the Private Service Connect endpoints of your Cloud SQL instances in a VPC network.

## April 09, 2025

Feature

Cloud SQL Enterprise Plus edition now supports a new machine series called the C4A machine series, which provides optimized price-performance and delivers predictable high performance for high demand Cloud SQL workloads. C4A uses a new type of storage called [Hyperdisk Balanced](https://docs.cloud.google.com/sql/docs/postgres/storage-options-overview), and offers up to 72 vCPUs and up to 576 GB memory. The C4A machine series is available in [Preview](https://cloud.google.com/products#product-launch-stages).

For more information about the C4A machine series and its availability, see [Machine series overview](https://docs.cloud.google.com/sql/docs/postgres/machine-series-overview).

Feature

Cloud SQL for Enterprise Plus edition supports [AI-assisted troubleshooting](https://docs.cloud.google.com/sql/docs/postgres/observe-troubleshoot-with-ai). With AI-assisted troubleshooting, you can resolve complex database performance issues like [slow queries](https://docs.cloud.google.com/sql/docs/postgres/troubleshoot-slow-queries) and [high load](https://docs.cloud.google.com/sql/docs/postgres/troubleshoot-high-database-load) for your instances in a guided manner. To use AI-assisted troubleshooting, you need [Gemini Cloud Assist](https://docs.cloud.google.com/gemini/docs/cloud-assist/overview) and [query insights for Enterprise Plus edition](https://docs.cloud.google.com/sql/docs/postgres/using-query-insights#enable-insights). AI-assisted troubleshooting is available in [Preview](https://cloud.google.com/products#product-launch-stages).

Feature

[Query insights for Cloud SQL Enterprise Plus edition](https://docs.cloud.google.com/sql/docs/postgres/using-query-insights#query-insights-for-enterprise-plus) is now generally available (GA) for your Cloud SQL Enterprise Plus edition for PostgreSQL instances. Query insights for Cloud SQL Enterprise Plus edition offers fine-grained metrics such as wait events and granular query plan samples for faster root-cause analysis and intelligent index recommendations.

For more information, see [Use query insights to improve query performance](https://docs.cloud.google.com/sql/docs/postgres/using-query-insights).

## April 04, 2025

Feature

The rollout of the following extension versions and plugin versions is complete:

**Extensions and plugins**

  * PostGIS is upgraded from 3.4.4 to 3.5.2.



To use these versions of the extensions, update your instance to `[PostgreSQL version]. R20250302.00_04`. 

If you use a maintenance window, then the updates to the minor, extension, and plugin versions happen according to the timeframe that you set in the window. Otherwise, the updates occur within the next few weeks.

For more information on checking your maintenance version, see [Self-service maintenance](https://docs.cloud.google.com/sql/docs/postgres/self-service-maintenance). To find your maintenance window or to manage maintenance updates, see [Find and set maintenance windows](https://docs.cloud.google.com/sql/docs/postgres/set-maintenance-window).

## March 31, 2025

Feature

Cloud SQL now supports Managed Connection Pooling (MCP) in [Preview](https://cloud.google.com/products#product-launch-stages), which lets you scale your workloads by optimizing resource utilization for your Cloud SQL instances using pooling. To use Managed Connection Pooling, update your instance to [`[PostgreSQL version].R20250302.00_04`](https://docs.cloud.google.com/sql/docs/postgres/maintenance-changelog).

For more information, see [Managed Connection Pooling overview](https://docs.cloud.google.com/sql/docs/postgres/managed-connection-pooling).

## March 25, 2025

Feature

Cloud SQL read pools provide operational simplicity and scaling for your large read workloads.

Read pools provide a single endpoint in front of up to 20 read pool nodes and automatically load balance traffic.

You can scale your read pool in several ways:

  * **Scale in or out** : scale load balancing capacity horizontally by modifying the number of read pool nodes in the read pool. Each read pool supports up to 20 read pool nodes.
  * **Scale up or down** : scale load balancing capacity vertically by modifying the machine type associated with a read pool node. Once defined, configuration is uniformly applied across each read pool node in the read pool.



For more information, see [About read pools](https://cloud.google.com/sql/docs/postgres/about-read-pools).

## March 24, 2025

Feature

Cloud SQL now lets you retain existing backups after an instance is deleted. These consist of on-demand and automatic backups created when the instance was live. For more information, see [Retained backups](https://docs.cloud.google.com/sql/docs/postgres/backup-recovery/backups#retained-backups).

## March 04, 2025

Feature

[Cloud SQL Enterprise edition](https://cloud.google.com/sql/docs/postgres/instance-settings) now supports the `europe-north2` (Stockholm) region.

## March 03, 2025

Feature

The rollout of the following minor versions, extension versions, and plugin versions is complete:

**Minor versions**

  * 12.21 is upgraded to 12.22.
  * 13.18 is upgraded to 13.20.
  * 14.15 is upgraded to 14.17.
  * 15.10 is upgraded to 15.12
  * 16.6 is upgraded to 16.8.
  * 17.2 is upgraded to 17.4.



**Extensions and plugins**

  * PostGIS is upgraded from 3.4.3 to 3.4.4.



To use these versions of the extensions, update your instance to `[PostgreSQL version].R20250112.01_14`. 

If you use a maintenance window, then the updates to the minor, extension, and plugin versions happen according to the timeframe that you set in the window. Otherwise, the updates occur within the next few weeks.

For more information on checking your maintenance version, see [Self-service maintenance](https://docs.cloud.google.com/sql/docs/postgres/self-service-maintenance). To find your maintenance window or to manage maintenance updates, see [Find and set maintenance windows](https://docs.cloud.google.com/sql/docs/postgres/set-maintenance-window).

## February 26, 2025

Feature

You can now include replicas when you perform an in-place major version upgrade using gcloud or the Cloud SQL Admin API. For more information, see [Upgrade the database major version in-place](https://docs.cloud.google.com/sql/docs/postgres/upgrade-major-db-version-inplace#include-replicas).

## February 25, 2025

Feature

You can now [export or import all user databases in an instance](https://cloud.google.com/sql/docs/postgres/import-export/import-export-parallel#export-entire-instance) using a directory-formatted, parallel export or import operation.

## February 20, 2025

Feature

You can now create a final backup of your data before you delete a Cloud SQL instance. You can use the final backup to restore your data to a new instance. This way, you can recover your data after you delete the instance. For more information, see [About Cloud SQL backups](https://docs.cloud.google.com/sql/docs/postgres/backup-recovery/backups#final-backups).

## February 12, 2025

Feature

Cloud SQL for PostgreSQL now supports the `tds_fdw` extension. This extension provides a foreign data wrapper (`fdw`) for accessing databases that use the Tabular Data Stream (TDS) protocol, such as Microsoft SQL Server or Sybase. Cloud SQL for PostgreSQL supports `tds_fdw` version 2.0.4. For more information about using this extension, see [Configure PostgreSQL extensions](https://docs.cloud.google.com/sql/docs/postgres/extensions).

You can now perform `pg_replication_origin_*` functions as a database user with the `cloudsqlsuperuser` role. For more information about `cloudsqlsuperuser`, see [About PostgreSQL users and roles](https://docs.cloud.google.com/sql/docs/postgres/users).

The rollout of the following extension version is underway:

  * `rdkit` is upgraded from 4.3.0 to 4.6.1



If you use a maintenance window, then the updates to the extension version happen according to the timeframe that you set in the window. Otherwise, the updates occur within the next few weeks.

The new maintenance version is `[PostgreSQL version].R20250112.01_03`. To learn how to check your maintenance version, see [Self-service maintenance](https://docs.cloud.google.com/sql/docs/postgres/self-service-maintenance). To find your maintenance window or to manage maintenance updates, see [Find and set maintenance windows](https://docs.cloud.google.com/sql/docs/postgres/set-maintenance-window).

## February 11, 2025

Feature

You can now use a custom DNS name to connect to your Cloud SQL instances by adding a custom subject alternative name (SAN) to your Cloud SQL instances. This feature is available for instances that are configured with Customer Managed CAS CA.. For more information, see [Create instances](https://docs.cloud.google.com/sql/docs/postgres/create-instance).

You can also add, modify, and remove a custom SAN for existing Cloud SQL instances. For more information, see [Edit instances](https://docs.cloud.google.com/sql/docs/postgres/edit-instance). 

This feature is available in [Preview](https://cloud.google.com/products#product-launch-stages).

## February 05, 2025

Feature

You can now migrate a subset of databases from an external server to a destination Cloud SQL instance. For more information, see [Configure Cloud SQL and the external server for replication](https://docs.cloud.google.com/sql/docs/postgres/replication/configure-replication-from-external).

Feature

You can now configure customer-managed CA (`CUSTOMER_MANAGED_CAS_CA`) as the server certificate authority (CA) mode when you create a Cloud SQL instance. With customer-managed CA mode, you set up your own CA pool and CA in [Certificate Authority Service](https://docs.cloud.google.com/certificate-authority-service/docs/ca-service-overview). This option lets you establish your own CA hierarchy and manage the rotation of CA certificates for your Cloud SQL instances to help you meet your regulatory compliance needs. 

To use the customer-managed CA option in Cloud SQL, see [Use a customer-managed certificate authority (CA)](https://docs.cloud.google.com/sql/docs/postgres/customer-managed-ca). For more information about server CA mode options, see [Certificate authority (CA) hierarchies](https://docs.cloud.google.com/sql/docs/postgres/authorize-ssl#ca-hierarchies). The customer-managed CA feature is in [Preview](https://cloud.google.com/products#product-launch-stages).

## February 01, 2025

Announcement

All Cloud SQL for PostgreSQL 9.6, 10, 11, and 12 instances are running community end-of-life (EOL) major versions and are now enrolled in Cloud SQL extended support.

**IMPORTANT** : Extended support is a paid service and is an addition to the current cost of your instance. Charges for extended support are waived from February 1, 2025 through April 30, 2025. Starting on May 1, 2025, all instances enrolled in extended support will be charged. To learn more about the benefits of extended support and pricing, see [Extended support for Cloud SQL](https://docs.cloud.google.com/sql/docs/postgres/extended-support).

## January 17, 2025

Feature

Cloud SQL for PostgreSQL version 17 adds support for the following extensions and plugins:

**Extensions and plugins**

  * ip4r
  * oracle_fdw
  * orafce
  * pg_background
  * pg_bigm
  * pgfincore
  * pg_hint_plan
  * pg_partman
  * pg_proctab
  * pgrouting
  * pg_similarity
  * pgtap
  * pgtt
  * pg_wait_sampling
  * PL/Proxy
  * plv8
  * postgresql_anonymizer
  * postgresql_hll
  * prefix
  * temporal_tables



Cloud SQL for PostgreSQL version 17 doesn't support:

  * rdkit
  * pg_squeeze



To use these extensions and plugins in your PostgreSQL 17 instance, update your instance to the `POSTGRES_17_2.R20241011.00_11` maintenance version. 

To learn how to check your maintenance version, see [Self service maintenance](https://docs.cloud.google.com/sql/docs/postgres/self-service-maintenance#before_you_begin/self-service-maintenance). To find your maintenance window or to manage maintenance updates, see [Find and set maintenance windows](https://docs.cloud.google.com/sql/docs/postgres/set-maintenance-window).

To start using PostgreSQL 17, see [Create instances](https://docs.cloud.google.com/sql/docs/postgres/create-instance).

## January 14, 2025

Feature

You can now migrate data from Microsoft Azure to Cloud SQL. For more information, see [Configure Cloud SQL and the external server for replication](https://docs.cloud.google.com/sql/docs/postgres/replication/configure-replication-from-external).

## December 23, 2024

Feature

The rollout of the following minor versions, extension versions, and plugin versions is **complete** :

**Minor versions**

  * 12.20 is upgraded to 12.21. This version restores functionality of the `ALTER {ROLE|DATABASE} SET role` command that's present in PostgreSQL version 12.22. For more information, see the [PostgreSQL 12.22 release notes](https://www.postgresql.org/docs/release/12.22/).
  * 13.16 is upgraded to 13.18.
  * 14.13 is upgraded to 14.15.
  * 15.8 is upgraded to 15.10.
  * 16.4 is upgraded to 16.6.
  * 17.0 is upgraded to 17.2.



**Extension and plugin versions**

  * orafce is upgraded from 4.7 to 4.73 (for PostgreSQL instances, versions 11-16).
  * pgAudit is upgraded from 17beta to 17.1 (for PostgreSQL instances, version 17).



To use these versions of the extensions, update your instance to one of the following:

  * `POSTGRES_17_0.R20241011.00_11` (for PostgreSQL instances, version 17)
  * `[PostgreSQL version].R20240910.01_31` (for PostgreSQL instances, versions 12 to 16)



If you use a maintenance window, then the updates to the minor, extension, and plugin versions happen according to the timeframe that you set in the window. Otherwise, the updates occur within the next few weeks.

For more information on checking your maintenance version, see [Self-service maintenance](https://docs.cloud.google.com/sql/docs/postgres/self-service-maintenance). To find your maintenance window or to manage maintenance updates, see [Find and set maintenance windows](https://docs.cloud.google.com/sql/docs/postgres/set-maintenance-window).

## December 20, 2024

Feature

You can now enable query insights for Cloud SQL Enterprise Plus edition. When you enable query insights for Enterprise Plus, you can access additional features in query insights such as 30 days of metrics retention, granular query plan details, and a higher query length limit. 

For more information, see [Use query insights to improve query performance](https://docs.cloud.google.com/sql/docs/postgres/using-query-insights#query-insights-for-enterprise-plus). Query insights for Cloud SQL Cloud SQL Enterprise Plus edition is in [Preview](https://cloud.google.com/products#product-launch-stages).

## December 10, 2024

Change

Cloud SQL now offers notifications for maintenance that's either started or completed. See the [Overview of maintenance on Cloud SQL](https://docs.cloud.google.com/sql/docs/postgres/maintenance#notifications) instances. To find out how to sign up for notifications and check your instances for upcoming maintenance, see [Find and set maintenance windows](https://docs.cloud.google.com/sql/docs/postgres/set-maintenance-window).

## December 05, 2024

Feature

[Cloud SQL Enterprise Plus edition](https://docs.cloud.google.com/sql/docs/editions-intro) now supports the following regions:

  * `africa-south1` (Johannesburg)
  * `asia-east2` (Hong Kong)
  * `europe-west10` (Berlin)



## December 03, 2024

Feature

You can now use the Network Connectivity Center hub to [propagate Private Service Connect endpoints](https://docs.cloud.google.com/sql/docs/postgres/about-private-service-connect#psc-endpoint-propagation) of Cloud SQL instances in a VPC network. All endpoints in this network become accessible transitively to other spoke VPC networks through the hub. This feature is available in [Preview](https://cloud.google.com/products#product-launch-stages).

## November 27, 2024

Feature

You can now create instances with both private services access and Private Service Connect enabled for them. You can also enable Private Service Connect for existing private services access instances. This feature is available in [Preview](https://cloud.google.com/products#product-launch-stages). For more information, see [Configure both private services access and Private Service Connect](https://docs.cloud.google.com/sql/docs/postgres/configure-private-services-access-and-private-service-connect).

## November 21, 2024

Feature

You can now set up AlloyDB clusters using a copy of your Cloud SQL for PostgreSQL backup. This feature is in [Preview](https://cloud.google.com/products#product-launch-stages). For more information, see [Migrate from Cloud SQL for PostgreSQL to AlloyDB](https://docs.cloud.google.com/sql/docs/postgres/backup-recovery/migrate-cloud-sql-to-alloydb).

## November 20, 2024

Feature

You can now authenticate to Cloud SQL Studio by using [IAM database authentication](https://docs.cloud.google.com/sql/docs/postgres/iam-authentication#iam-db-auth).

For more information about authentication in Cloud SQL Studio, see [Manage your data using Cloud SQL Studio](https://docs.cloud.google.com/sql/docs/postgres/manage-data-using-studio#authentication).

## November 19, 2024

Feature

The write endpoint feature is now available in [Preview](https://cloud.google.com/products#product-launch-stages). This endpoint is a global domain name service (DNS) name. This name resolves to the IP address of the current primary Cloud SQL instance that's enabled with private services access. 

By using a write endpoint, you can avoid having to make application connection changes after performing a switchover or replica failover operation to test or mitigate a regional failure. For more information, see [Configure private IP](https://docs.cloud.google.com/sql/docs/postgres/configure-private-ip#connect-write-endpoint).

Feature

For [Cloud SQL Enterprise Plus edition](https://docs.cloud.google.com/sql/docs/postgres/editions-intro) instances, you can now use advanced disaster recovery (DR) to simplify recovery and fallback processes after you perform a cross-regional failover. With advanced DR, you can: 

  * Designate a cross-region disaster recovery (DR) replica
  * Perform a cross-region replica failover for disaster recovery
  * Restore your original deployment by using zero-data loss switchover



You can also use switchover to simulate disaster recovery without data loss. You can use advanced DR on Cloud SQL for PostgreSQL version 12, 13, 14, 15, or 16.

For more information, see [Advanced disaster recovery (DR)](https://docs.cloud.google.com/sql/docs/postgres/intro-to-cloud-sql-disaster-recovery#advanced-dr) and [Use advanced disaster recovery (DR)](https://docs.cloud.google.com/sql/docs/postgres/use-advanced-disaster-recovery). This feature is [generally available](https://cloud.google.com/products#product-launch-stages) (GA).

## November 18, 2024

Feature

The `pgvector` extension is now upgraded from version 0.7.4 to version 0.8.0. Use this extension to store and search for vector embeddings in PostgreSQL databases. For more information, see [Configure PostgreSQL extensions](https://cloud.google.com/sql/docs/postgres/extensions). 

To use this version of the extension, update your instance to one of the following:

  * `POSTGRES_17_0.R20241011.00_03` (for PostgreSQL instances, version 17)
  * `[PostgreSQL version].R20240910.01_17` (for PostgreSQL instances, versions 13 to 16)



For more information, see [Self-service maintenance](https://docs.cloud.google.com/sql/docs/postgres/self-service-maintenance).

Feature

Cloud SQL now supports near-zero downtime for infrequent scale downs (once every three hours) of the compute size (vCPU, memory) of your Cloud SQL Enterprise Plus edition primary instance.

For more information, see [Availability in Cloud SQL](https://docs.cloud.google.com/sql/docs/postgres/availability#planned_operations_with_near-zero_downtime).

Feature

Cloud SQL now supports near-zero downtime when you enable or disable [data cache](https://docs.cloud.google.com/sql/docs/postgres/data-cache) for Cloud SQL Enterprise Plus edition primary instances. For more information, see [Availability in Cloud SQL](https://docs.cloud.google.com/sql/docs/postgres/availability#planned_operations_with_near-zero_downtime).

Feature

Support for the [northamerica-south1](https://docs.cloud.google.com/sql/docs/postgres/locations) (Mexico) region.

## November 15, 2024

Feature

You can now register an AI model endpoint, generate vector embeddings, and invoke predictions by using model endpoint management in Cloud SQL. For more information, see [Register and call remote AI models in Cloud SQL overview](https://docs.cloud.google.com/sql/docs/postgres/model-endpoint-overview).

## November 14, 2024

Feature

You can now create custom organization policies for the [`BackupRun`](https://docs.cloud.google.com/sql/docs/postgres/admin-api/rest/v1/backupRuns) resource in Cloud SQL instances. In addition, more fields in the [`Instances`](https://docs.cloud.google.com/sql/docs/postgres/admin-api/rest/v1/instances) resource are available to create custom organization policies. For more information, see [Add custom organization policies](https://docs.cloud.google.com/sql/docs/postgres/org-policy/custom-org-policy).

## November 12, 2024

Feature

You can now have Cloud SQL create a Private Service Connect endpoint automatically instead of creating the endpoint manually after the instance is created. You use this endpoint to access a Cloud SQL instance through a VPC network. For more information, see [Connect to an instance using Private Service Connect](https://docs.cloud.google.com/sql/docs/postgres/configure-private-service-connect#create-endpoint-automatically). This feature is available in [Preview](https://cloud.google.com/products?e=48754805#product-launch-stages).

## November 04, 2024

Feature

You can now [view the size of a backup](https://docs.cloud.google.com/sql/docs/postgres/backup-recovery/backing-up#view-backup-size) for a Cloud SQL instance.

## October 25, 2024

Feature

When you run the [`backupRuns.GET` API](https://docs.cloud.google.com/sql/docs/postgres/admin-api/rest/v1/backupRuns/get) or the [`gcloud sql backups describe`](https://docs.cloud.google.com/sdk/gcloud/reference/sql/backups/describe) command, the `maxChargeableBytes` parameter now appears in the response. This parameter contains the maximum number of bytes that you can be charged for a backup.

## October 23, 2024

Feature

PostgreSQL version 17 is now [generally available](https://cloud.google.com/products#product-launch-stages).

When using the CLI/API to create an instance, if the database version for the instance or replica that you're creating is PostgreSQL 16 and later, then the default Cloud SQL edition is Enterprise Plus.

When using the CLI/API to create an instance, If you either don't specify a database version or you specify a version other than PostgreSQL 16 and later, then the default Cloud SQL edition is Enterprise.

The following information applies to **flags** and **extensions** for PostgreSQL 17:

**Flags**

These flags are deprecated for PostgreSQL 17:

  * old_snapshot_threshold
  * trace_recovery_messages



For more information, see [Configure database flags](https://docs.cloud.google.com/sql/docs/postgres/flags).

**Extensions**

Cloud SQL for PostgreSQL version 17 doesn't support these extensions:

  * ip4r 
  * oracle_fdw 
  * orafce
  * pg_background 
  * pg_bigm 
  * pgfincore 
  * pg_hint_plan 
  * pg_partman 
  * pg_proctab
  * pgrouting 
  * pg_similarity 
  * pg_squeeze
  * pgtap 
  * pgtt 
  * pg_wait_sampling
  * PL/Proxy 
  * plv8 
  * postgresql_anonymizer 
  * postgresql_hll
  * prefix
  * rdkit 
  * temporal_tables



To start using PostgreSQL 17, see [Create instances](https://docs.cloud.google.com/sql/docs/postgres/create-instance).

## October 21, 2024

Feature

You can now create a read replica for an instance that has [private services access](https://docs.cloud.google.com/sql/docs/postgres/configure-private-services-access#configure-access) configured for it and [connector enforcement](https://docs.cloud.google.com/sql/docs/postgres/admin-api/rest/v1/instances#ConnectorEnforcement) enabled for it. For more information, see [Connect using Cloud SQL Language Connectors](https://docs.cloud.google.com/sql/docs/postgres/connect-connectors#enforce).

## October 03, 2024

Feature

You can now configure server certificate authority (CA) mode when you create a Cloud SQL instance. With server CA mode, you have two options:

  * **Per-instance CA** : this is the default configuration. With this option, an internal CA dedicated to each Cloud SQL instance signs the server certificate for that instance.
  * **Shared CA** : with this option, the Cloud SQL instance uses a CA hierarchy consisting of a root CA and subordinate server CAs managed by Cloud SQL and hosted on Google Cloud Certificate Authority Service (CA Service). The subordinate server CAs in a region sign the server certificates and are shared across instances in the region. 



For more information about each option, see [Certificate authority (CA) hierarchies](https://docs.cloud.google.com/sql/docs/postgres/authorize-ssl#certificate_authority_ca_hierarchies). This feature is in [Preview](https://cloud.google.com/products#product-launch-stages).

Feature

The `pg_ivm` extension, version 1.9, is generally available. This extension enables you to make materialized views up-to-date in which only incremental changes are computed and applied on views rather than recomputing the contents from scratch. 

Cloud SQL for PostgreSQL, version 16, now supports the `pgRouting` extension. This extension extends PostGIS and enhances geospatial processing through network routing and analysis.

For more information on these extensions, see [Configure PostgreSQL extensions](https://docs.cloud.google.com/sql/docs/postgres/extensions).

The rollout of the following minor versions, extension versions, and plugin versions is **underway** :

**Minor versions**

  * 12.19 is upgraded to 12.20.
  * 13.15 is upgraded to 13.16.
  * 14.12 is upgraded to 14.13.
  * 15.7 is upgraded to 15.8.
  * 16.3 is upgraded to 16.4.



**Extension and plugin versions**

  * google_ml_integration is upgraded from 1.2 to 1.4.2.
  * pgvector is upgraded from 0.7.0 to 0.7.4.



If you use a maintenance window, then the updates to the minor, extension, and plugin versions happen according to the timeframe that you set in the window. Otherwise, the updates occur within the next few weeks.

The new maintenance version is `[PostgreSQL version].R20240910.01.00_02`. To learn how to check your maintenance version, see [Self service maintenance](https://docs.cloud.google.com/sql/docs/postgres/self-service-maintenance#before_you_begin/self-service-maintenance). To find your maintenance window or to manage maintenance updates, see [Find and set maintenance windows](https://docs.cloud.google.com/sql/docs/postgres/set-maintenance-window).

## September 25, 2024

Feature

You can now set up AlloyDB free trial clusters using a copy of your Cloud SQL for PostgreSQL backup. For more information, see [Migrate from Cloud SQL for PostgreSQL to AlloyDB](https://docs.cloud.google.com/sql/docs/postgres/backup-recovery/migrate-cloud-sql-to-alloydb).

## September 19, 2024

Feature

You can now use gcloud or the Cloud SQL Admin API to switch the storage location of the transaction logs used for point-in-time recovery on your instance without downtime to Cloud Storage. For more information, see [Use point-in-time recovery](https://docs.cloud.google.com/sql/docs/postgres/backup-recovery/pitr) and [Switch transaction log storage to Cloud Storage](https://docs.cloud.google.com/sql/docs/postgres/backup-recovery/pitr#switch-to-gcs).

## September 12, 2024

Feature

You can now upgrade your instances to Cloud SQL Enterprise Plus edition with near-zero downtime. To upgrade your instance, see [Upgrade an instance to Cloud SQL Enterprise Plus edition using in-place upgrade](https://docs.cloud.google.com/sql/docs/postgres/upgrade-cloud-sql-instance-to-enterprise-plus-in-place).

Feature

You can now provide access to Cloud SQL Studio by granting a new IAM role, Cloud SQL Studio User (`roles/cloudsql.studioUser`), instead of using the Cloud SQL Admin IAM role.

For more information about using Cloud SQL Studio, see [Manage your data using Cloud SQL Studio](https://docs.cloud.google.com/sql/docs/postgres/manage-data-using-studio).

Feature

Cloud SQL now supports near-zero downtime planned maintenance on standalone Cloud SQL Enterprise Plus edition primary instances. In addition, you can also simulate near-zero downtime for planned maintenance events on standalone Cloud SQL Enterprise Plus edition primary instances.

For more information, see [About maintenance on Cloud SQL instances](https://docs.cloud.google.com/sql/docs/postgres/maintenance).

## September 03, 2024

Feature

You can now use point-in-time recovery to restore your zonal instance to a preferred primary zone and your regional instance to both a preferred primary zone and a preferred secondary zone. For more information, see [Use point-in-time recovery (PITR)](https://docs.cloud.google.com/sql/docs/postgres/backup-recovery/pitr).

When you clone your zonal instance, you can now specify a preferred zone for the instance. You can also specify preferred primary and secondary zones for your regional instance. If the zones for your instance go down in the future, then Cloud SQL can assign the preferred zones to the instance, and you don't experience downtime. For more information, see [Clone instances](https://docs.cloud.google.com/sql/docs/postgres/clone-instance).

## August 15, 2024

Announcement

Extended support pricing is now available for Cloud SQL for PostgreSQL. To view pricing details, see [Cloud SQL pricing](https://cloud.google.com/sql/pricing#extended-support-pricing).

For more information about extended support, see [Extended support for Cloud SQL](https://docs.cloud.google.com/sql/docs/postgres/extended-support).

For more information about extended support timelines, see [Database versions and version policies](https://docs.cloud.google.com/sql/docs/postgres/db-versions).

Change

If your Cloud SQL Enterprise edition instance stores the transaction logs used for point-in-time recovery (PITR) on disk, then when you do an in-place upgrade to Cloud SQL Enterprise Plus edition the storage location for the transaction logs is switched to Cloud Storage. For more information, see [Upgrade an instance to Cloud SQL Enterprise Plus edition by using in-place upgrade](https://docs.cloud.google.com/sql/docs/postgres/upgrade-cloud-sql-instance-to-enterprise-plus-in-place).

To check where your instance stores the transaction logs used for PITR, see [Use point-in-time recovery (PITR)](https://docs.cloud.google.com/sql/docs/postgres/backup-recovery/pitr#check-log-storage-location).

## July 31, 2024

Feature

Gemini in Databases assistance in Cloud SQL for PostgreSQL is now available in [Preview](https://cloud.google.com/products#product-launch-stages) for query insights, system insights, index advisor, and active queries. You can use Gemini assistance to help you observe and troubleshoot your Cloud SQL resources. For more information, see [Observe and troubleshoot with Gemini assistance](https://docs.cloud.google.com/sql/docs/postgres/observe-troubleshoot-with-gemini).

## July 26, 2024

Feature

[IAM group authentication](https://docs.cloud.google.com/sql/docs/postgres/iam-authentication#iam-group-auth) is now generally available (GA) for Cloud SQL for PostgreSQL. You can [add IAM groups to Cloud SQL instances](https://docs.cloud.google.com/sql/docs/postgres/add-manage-iam-users#add-iam-group-db) and manage database access at the group level. To use IAM group authentication, you must have `[PostgreSQL version].R20240514.00_04` or later installed on your instance.

Feature

[Migrate to AlloyDB insight recommendations](https://docs.cloud.google.com/sql/docs/postgres/recommender-alloydb) are available in [Preview](https://cloud.google.com/products?e=48754805#product-launch-stages).

## July 25, 2024

Change

You can now upgrade the network architecture of a Cloud SQL instance that isn't enabled with [high-availability](https://docs.cloud.google.com/sql/docs/postgres/high-availability). The previous limitation on upgrading the network architecture of these instances is removed. To check whether your Cloud SQL instance has high availability enabled, see [Verify an instance's high availability configuration](https://docs.cloud.google.com/sql/docs/postgres/configure-ha#verify-ha).

For more information about upgrading your network architecture, see [Upgrade an instance to the new network architecture](https://docs.cloud.google.com/sql/docs/postgres/upgrade-cloud-sql-instance-new-network-architecture).

## July 18, 2024

Feature

You can now create custom organization policies for Cloud SQL instances. For more information, see [Add custom organization policies](https://docs.cloud.google.com/sql/docs/postgres/org-policy/custom-org-policy).

## July 17, 2024

Feature

You can now use the following optional flags when you export and import files into Cloud SQL instances:

  * `--clean`: if you export files, then this flag enables you to include the `DROP <object>` SQL statement that's required to drop (clean) database objects before you import them. If you import files, then this flag enables you to clean database objects before you recreate them. 
  * `--if-exists`: this flag enables you to include the `IF EXISTS` SQL statement with each `DROP` statement that's produced by the `clean` flag.



If you import files, then these flags apply only if you use the `--parallel` flag. If you export files, then use these flags only if you're not [exporting files in parallel](https://docs.cloud.google.com/sql/docs/postgres/import-export/import-export-parallel).

## July 16, 2024

Feature

Cloud SQL Studio is now [generally available](https://cloud.google.com/products#product-launch-stages). For more information, see [Manage your data using Cloud SQL Studio](https://docs.cloud.google.com/sql/docs/postgres/manage-data-using-studio).

Feature

You can now search for and manage your Cloud SQL resources by using [Dataplex Catalog](https://docs.cloud.google.com/dataplex/docs/catalog-overview). For more information about the integration of Cloud SQL and Dataplex Catalog, see [Manage your Cloud SQL resources using Dataplex Catalog](https://docs.cloud.google.com/sql/docs/postgres/dataplex-catalog-integration).

## July 02, 2024

Feature

[Cloud SQL Enterprise Plus edition](https://docs.cloud.google.com/sql/docs/editions-intro) now supports the southamerica-west1 (Santiago) region.

## June 21, 2024

Feature

You can now use the [in-place major version upgrade](https://docs.cloud.google.com/sql/docs/postgres/upgrade-major-db-version-inplace) feature to upgrade your Cloud SQL for PostgreSQL instance to PostgreSQL 16.

## June 20, 2024

Feature

You can now use the `gcloud sql instances describe` command or the SQL Admin API to retrieve a list of database versions that are available to your PostgreSQL instance for upgrade. For more information, see [Plan a major version upgrade](https://docs.cloud.google.com/sql/docs/postgres/upgrade-major-db-version-inplace#plan-upgrade).

## June 10, 2024

Feature

The `temporal_tables` extension, version 1.2.2 is generally available. This extension provides support for temporal tables. A temporal table records the period of time when a row is valid from a database perspective. For more information, see [Configure PostgreSQL extensions](https://docs.cloud.google.com/sql/docs/postgres/extensions).

You can now perform `CREATE CAST` and `DROP CAST` statements as a database user with the `cloudsqlsuperuser` role. For more information, see [About PostgreSQL users and roles](https://docs.cloud.google.com/sql/docs/postgres/users).

The rollout of the following minor versions, extension versions, and plugin versions is **underway** :

**Minor versions**

  * 12.17 is upgraded to 12.19.
  * 13.13 is upgraded to 13.15.
  * 14.10 is upgraded to 14.12.
  * 15.5 is upgraded to 15.7.



**Extension and plugin versions**

  * google_ml_integration is upgraded from 1.2 to 1.3.
  * pg_partman is upgraded from 4.7.4 to 5.0.1 (for PostgreSQL versions 14 and later).
  * pgvector is upgraded from 0.6.0 to 0.7.0.
  * Plv8 is upgraded from 3.2.0 to 3.2.2.
  * PostGIS is upgraded from 3.2.5 to 3.4.0 (for PostgreSQL versions 12 and later).



If you use a maintenance window, then the updates to the minor, extension, and plugin versions happen according to the timeframe that you set in the window. Otherwise, the updates occur within the next few weeks.

The new maintenance version is `[PostgreSQL version].R20240514.00_04`. To learn how to check your maintenance version, see [Self service maintenance](https://docs.cloud.google.com/sql/docs/postgres/self-service-maintenance#before_you_begin/self-service-maintenance). To find your maintenance window or to manage maintenance updates, see [Find and set maintenance windows](https://docs.cloud.google.com/sql/docs/postgres/set-maintenance-window).

Feature

You can now choose to receive a maintenance notification 5 weeks before the maintenance update of your Cloud SQL instance is scheduled to occur. This option is named **Week 5**.

In addition, some labels in the Google Cloud Console have been renamed to align with this new option:

  * **Order of update** is renamed to **Maintenance timing**
  * **Earlier** is renamed to **Week 1**
  * **Later** is renamed to **Week 2**



For more information, see [Maintenance settings](https://docs.cloud.google.com/sql/docs/postgres/maintenance#management) and [Find and set maintenance windows](https://docs.cloud.google.com/sql/docs/postgres/set-maintenance-window).

## June 07, 2024

Feature

PostgreSQL version 16 is now generally available.

When you use gcloud or the API to create an instance or replica, the following conditions now apply:

  * If the database version for the instance or replica that you're creating is PostgreSQL 16, then the default Cloud SQL edition is Enterprise Plus. 
  * If you either don't specify a database version or you specify a version other than PostgreSQL 16, then the default Cloud SQL edition is Enterprise.



You can't use the in place major version upgrade feature to upgrade your Cloud SQL for PostgreSQL instance to PostgreSQL 16.

To start using PostgreSQL 16, see [Create instances](https://docs.cloud.google.com/sql/docs/postgres/create-instance).

## May 29, 2024

Announcement

Cloud SQL for PostgreSQL major versions that have reached community end-of-life (EOL) will receive extended support starting on February 1, 2025. For more information about extended support, see [Extended support for Cloud SQL](https://docs.cloud.google.com/sql/docs/postgres/extended-support). 

For more information about extended support timelines, see [Database versions and version policies](https://docs.cloud.google.com/sql/docs/postgres/db-versions).

## May 23, 2024

Breaking

Monitoring active queries in Cloud SQL for PostgreSQL, which is part of the Gemini in Databases Preview, is temporarily unavailable. You can still monitor completed queries. For more information about monitoring queries, see [Use Query Insights to improve query performance](https://docs.cloud.google.com/sql/docs/postgres/using-query-insights).

## April 22, 2024

Announcement

The `pgvector` extension is upgraded from version 0.5.1 to version 0.6.0. Use this extension to store and search for vector embeddings in PostgreSQL databases. For more information, see [Configure PostgreSQL extensions](https://docs.cloud.google.com/sql/docs/postgres/extensions). 

To use this version of the extension, update your instance to `[PostgreSQL version].R20240130.00_09`. For more information, see [Self-service maintenance](https://docs.cloud.google.com/sql/docs/postgres/self-service-maintenance).

## April 09, 2024

Feature

The following [Gemini in Databases](https://docs.cloud.google.com/gemini/docs/databases/overview) features are now available in Public Preview:

  * [Database Center](https://docs.cloud.google.com/database-center/docs/overview): an AI-assisted dashboard that gives you one centralized view across your entire database fleet.
  * [Cloud SQL Studio](https://docs.cloud.google.com/sql/docs/postgres/manage-data-using-studio): lets authorized users interact directly with the SQL database and run SQL queries from the Google Cloud console to access and manipulate data.
  * [Monitor active queries](https://docs.cloud.google.com/sql/docs/postgres/monitor-active-queries): monitor and troubleshoot the queries that are active in your database.
  * [Index advisor](https://docs.cloud.google.com/sql/docs/postgres/index-advisor-overview): a fully managed index advisor that tracks the queries your database handles regularly.
  * 4-week query metric retention in the [Query Insights dashboard](https://docs.cloud.google.com/sql/docs/mysql/using-query-insights).
  * 15 new database insight recommendations.



To learn how to enable and activate Gemini in Databases, see [Set up Gemini in Databases](https://docs.cloud.google.com/gemini/docs/databases/set-up-gemini).

## April 08, 2024

Feature

[Cloud SQL Enterprise Plus edition](https://docs.cloud.google.com/sql/docs/postgres/editions-intro) primary instances with high availability (HA) now require less than one second of downtime for [planned maintenance](https://docs.cloud.google.com/sql/docs/postgres/maintenance#nearzero).

## April 03, 2024

Feature

You can now [migrate data in the tables of your database in parallel](https://docs.cloud.google.com/sql/docs/postgres/replication/managed-import-replication-from-external). There's a performance improvement because Cloud SQL can transfer the data with parallel processes within a database. You can set the speed that Cloud SQL transfers this data to `min`, `optimal`, or `max`.

## April 02, 2024

Change

Version 0.6.0 of the `pgvector` extension that's listed in the [March 27](https://docs.cloud.google.com/sql/docs/postgres/release-notes#March_27_2024) release note isn't available yet. Use version 0.5.1 of this extension.

Feature

You can now scale up the compute size (vCPU, memory) of a [Cloud SQL Enterprise Plus edition](https://docs.cloud.google.com/sql/docs/postgres/editions-intro) primary instance with near-zero downtime.

## March 28, 2024

Feature

You can now simulate a planned maintenance update with near-zero downtime on your [Cloud SQL Enterprise Plus](https://docs.cloud.google.com/sql/docs/postgres/editions-intro) primary instance without updating your database. For more information, see [About maintenance on Cloud SQL instances](https://docs.cloud.google.com/sql/docs/postgres/maintenance#simulate-zdt).

## March 27, 2024

Announcement

The `pgvector` extension is upgraded from version 0.5.1 to version 0.6.0. Use this extension to store and search for vector embeddings in PostgreSQL databases. For more information, see [Configure PostgreSQL extensions](https://docs.cloud.google.com/sql/docs/postgres/extensions). 

To use this version of the extension, update your instance to `[PostgreSQL version].R20240130.00_07`. For more information, see [Self-service maintenance](https://docs.cloud.google.com/sql/docs/postgres/self-service-maintenance).

Announcement

The rollout of the following items in the [February 7](https://docs.cloud.google.com/sql/docs/postgres/release-notes#February_07_2024) release note is now **complete** :

  * Extensions
  * Flags
  * Minor versions
  * Extension versions
  * Plugin versions



## March 26, 2024

Feature

You can now integrate Cloud SQL and Vertex AI. This integration lets you apply large language models (LLMs), which are hosted in Vertex AI, to a Cloud SQL for PostgreSQL database, version 12 and later. For more information, see [Integrate Cloud SQL with Vertex AI](https://docs.cloud.google.com/sql/docs/postgres/integrate-cloud-sql-with-vertex-ai).

## March 25, 2024

Feature

Private Service Connect now includes support for [cross-region read replicas](https://docs.cloud.google.com/sql/docs/postgres/replication/create-replica#create-read-replica-cloud-sql-instance-psc-enabled). You can also [choose an availability type](https://docs.cloud.google.com/sql/docs/postgres/configure-ha) (REGIONAL or ZONAL) for Private Service Connect-enabled instances. Both features are in [GA](https://cloud.google.com/products?hl=en#product-launch-stages).

## March 19, 2024

Feature

[Cloud SQL Enterprise Plus edition](https://docs.cloud.google.com/sql/docs/editions-intro) now supports the me-central2 (Dammam) region.

## March 05, 2024

Feature

You can now upgrade network architecture for your HA-enabled instances in a region, even if you have multiple instances in your network and region. For more information, see [Upgrade an instance to the new network architecture](https://docs.cloud.google.com/sql/docs/postgres/upgrade-cloud-sql-instance-new-network-architecture).

## March 04, 2024

Announcement

The new maintenance version listed in the [February 7th](https://docs.cloud.google.com/sql/docs/postgres/release-notes#February_07_2024) entry for PostgreSQL extensions, flags, minor versions, extension versions, and plugin versions is `[PostgreSQL version].R20240130.00_05`.

## February 20, 2024

Feature

Cloud SQL Enterprise Plus edition now supports versions 12 and 13 of PostgreSQL. For more information, see [Introduction to Cloud SQL editions](https://docs.cloud.google.com/sql/docs/editions-intro).

## February 09, 2024

Feature

Cloud SQL now automatically updates your read replicas when you perform self-service maintenance on the primary instance. For more information, see [Self-service maintenance](https://docs.cloud.google.com/sql/docs/postgres/self-service-maintenance).

## February 08, 2024

Feature

Cloud SQL now supports near-zero downtime planned maintenance on HA-enabled Cloud SQL Enterprise Plus instances with all combinations of public IP connectivity.

## February 07, 2024

Feature

The rollout of the following extensions and flags is **underway** :

**Extensions**

  * **autoinc** (version 1.0): provides functions for incrementing fields automatically. This trigger stores the next value of a sequence into an integer field.
  * **bloom** (version 1.0): provides a method to access indexes based on bloom filters. These filters are space-efficient data structures that you can use to test whether an element is a member of a set.
  * **insert_username** (version 1.0): provides functions for storing the current user's name into a text field. You can use this to track who last modified a row in a database table.
  * **moddatetime** (version 1.0): provides functions for storing the current time into a timestamp field. You can use this to track the last time that a row in a database table is modified.
  * **pg_background** (version 1.2): lets you run arbitrary commands in a background worker.
  * **pg_squeeze** (version 1.5): removes unused space from a table and lets you use an index to sort records or rows (tuples) of the table.
  * **tcn** (version 1.0): provides a trigger function that notifies listeners of changes to the content of database tables.



**Flags**

  * **cloudsql.enable_pg_squeeze** : enables the `pg_squeeze` extension for Cloud SQL for PostgreSQL
  * **squeeze.max_xlock_time** : sets the time (in milliseconds) that the extension uses to finalize the processing for modifying a table
  * **squeeze.worker_autostart** : starts a background worker automatically
  * **squeeze.worker_role** : specifies the role for the background worker



The rollout of the following minor versions, extension versions, and plugin versions is **underway** :

**Minor versions**

  * 11.21 is upgraded to 11.22.
  * 12.16 is upgraded to 12.17.
  * 13.12 is upgraded to 13.13.
  * 14.9 is upgraded to 14.10.
  * 15.4 is upgraded to 15.5.



**Extension and plugin versions**

  * ipr4 is upgraded from 2.4.1 to 2.4.2.
  * orafce is upgraded, as follows: 
    * from 3.25.1 to 4.6.1 (for PostgreSQL versions 9.6 and 10)
    * from 4.6.1 to 4.7.0 (for PostgreSQL versions 11 and later)
  * pg_cron is upgraded from 1.5.2 to 1.6.0.
  * pgfincore is upgraded from 1.2.3 to 1.3.1.
  * pg_partman is upgraded from 4.7.3 to 4.7.4.
  * pg_repack is upgraded from 1.4.8 to 1.5.0.
  * pgTAP is upgraded from 1.2.0 to 1.3.0.
  * pgtt is upgraded from 2.9.0 to 3.0.
  * pg_wait_sampling is upgraded from 1.1.4 to 1.1.5.
  * PL/Proxy is upgraded from 2.10.0 to 2.11.0.
  * plv8 is upgraded from 3.1.4 to 3.2.0.
  * postgresql_hll is upgraded from 2.17 to 2.18.



If you use a maintenance window, then the updates to the minor, extension, and plugin versions happen according to the timeframe that you set in the window. Otherwise, the updates occur within the next few weeks.

The new maintenance version is `[PostgreSQL version].R20240130.00_00`. To learn how to check your maintenance version, see [Self service maintenance](https://docs.cloud.google.com/sql/docs/postgres/self-service-maintenance#before_you_begin/self-service-maintenance). To find your maintenance window or to manage maintenance updates, see [Find and set maintenance windows](https://docs.cloud.google.com/sql/docs/postgres/set-maintenance-window).

## February 01, 2024

Feature

Private Service Connect now includes support for cross-region read replicas. You can also choose an availability type (REGIONAL or ZONAL) for Private Service Connect-enabled instances. Both features are in [Preview](https://cloud.google.com/products#product-launch-stages). 

For more information, see [Connect to an instance using Private Service Connect](https://docs.cloud.google.com/sql/docs/postgres/configure-private-service-connect).

## January 31, 2024

Feature

Support for [africa-south1](https://docs.cloud.google.com/sql/docs/postgres/locations) (Johannesburg) region.

## January 30, 2024

Feature

You can now use the `pg_dump` and `pg_restore` utilities to export and import data for multiple files in parallel. For more information, see [Export and import files in parallel](https://docs.cloud.google.com/sql/docs/postgres/import-export/import-export-parallel).

## January 25, 2024

Feature

[Cloud SQL Enterprise Plus edition](https://docs.cloud.google.com/sql/docs/editions-intro) now supports the following regions:

  * asia-northeast2 (Osaka)
  * asia-south2 (Delhi)
  * europe-north1 (Finland)
  * europe-southwest1 (Madrid)
  * us-east5 (Columbus)
  * us-south1 (Dallas)



## December 18, 2023

Feature

[Cloud SQL Enterprise Plus edition](https://cloud.google.com/sql/docs/editions-intro) now supports the following regions:

  * europe-west8 (Milan)
  * europe-west12 (Turin)
  * us-west4 (Las Vegas)



## December 14, 2023

Feature

You can now use Database Migration Service to [migrate data](https://docs.cloud.google.com/sql/docs/postgres/migrate-data-to-cloud-sql-instance) to an existing Cloud SQL instance that was created using Terraform or other Infrastructure-As-Code (IaC) Tools.

## December 13, 2023

Feature

The following [flags](https://cloud.google.com/sql/docs/postgres/flags) are generally available:

  * **autovacuum_vacuum_insert_scale_factor** : specify a fraction of the size of a database table to add to the `autovacuum_vacuum_insert_threshold` flag. Use this flag when you're deciding whether to run a [`VACUUM`](https://www.postgresql.org/docs/current/sql-vacuum.html). 
  * **autovacuum_vacuum_insert_threshold** : specify the minimum number of inserted records or rows (tuples) that you need to run a `VACUUM` in any database table.
  * **effective_io_concurrency** : set the number of concurrent disk I/O operations that can run simultaneously.
  * **hash_mem_multiplier** : compute the maximum amount of memory that hash-based operations can use.
  * **logical_decoding_work_mem** : specify the maximum amount of memory that logical decoding can use before some of the decoded changes are written to a local disk.
  * **maintenance_io_concurrency** : set the number of concurrent disk I/O operations that can run simultaneously for maintenance work that's done for client sessions.
  * **vacuum_failsafe_age** : specify the maximum age (in transactions) that a database table's [`pg_class.relfrozenxid`](https://www.postgresql.org/docs/current/catalog-pg-class.html) field can attain before a `VACUUM` takes extraordinary measures to avoid a system-wide wraparound failure for transaction IDs. 
  * **vacuum_multixact_failsafe_age** : specify the maximum age (in multiple transactions) that a database table's [`pg_class.relminmxid`](https://www.postgresql.org/docs/current/catalog-pg-class.html) field can attain before a `VACUUM` takes extraordinary measures to avoid a system-wide wraparound failure for multiple transaction IDs.



## December 11, 2023

Feature

The `pgvector` extension, version 0.5.1 is generally available. Use this extension to store and search for vector embeddings in PostgreSQL databases. For more information, see [Configure PostgreSQL extensions](https://docs.cloud.google.com/sql/docs/postgres/extensions).

## December 08, 2023

Feature

You can now upgrade your Cloud SQL instances to use the new network architecture to get additional capabilities not available in the old network architecture. For more information, see [Upgrade an instance to the new network architecture](https://docs.cloud.google.com/sql/docs/postgres/upgrade-cloud-sql-instance-new-network-architecture).

## November 17, 2023

Feature

Cloud SQL now supports migrating data to an instance that already exists. You can create the instance by using Terraform or other Infrastructure-As-Code (IaC) Tools. After creating the instance, use the [demote](https://docs.cloud.google.com/sql/docs/postgres/admin-api/rest/v1/instances/demote) API to migrate data to it. This API demotes an existing standalone instance to be a Cloud SQL read replica for an external database server.

## November 10, 2023

Feature

You can now upgrade Enterprise edition instances to Enterprise Plus edition in place with minimal disruption. Similarly, you can also switch from Enterprise Plus edition to Enterprise edition in place. For more information, see [Upgrade an instance by using in-place upgrade](https://docs.cloud.google.com/sql/docs/postgres/upgrade-cloud-sql-instance-to-enterprise-plus-in-place).

## November 09, 2023

Feature

[Data cache](https://docs.cloud.google.com/sql/docs/postgres/data-cache) is now available for Cloud SQL for PostgreSQL Enterprise Plus edition instances.

## November 06, 2023

Feature

[Cloud SQL Enterprise Plus edition](https://docs.cloud.google.com/sql/docs/editions-intro) now supports asia-southeast2 (Jakarta).

## October 30, 2023

Feature

The rollout of the following items is **complete** :

  * The `oracle_fdw` extension, version 1.2 
  * The minor versions, extension versions, and plugin versions listed in the [September 21](https://docs.cloud.google.com/sql/docs/postgres/release-notes#September_21_2023) release note



## October 27, 2023

Feature

You can now specify the SSL mode of your Cloud SQL instances, which gives you more accurate SSL encryption. To use SSL mode, you must use the maintenance version [PostgreSQL version].R20230530.01_00 or newer. For more information, see [Enforce SSL/TLS encryption](https://docs.cloud.google.com/sql/docs/postgres/configure-ssl-instance#enforcing-ssl).

## October 02, 2023

Change

For Cloud SQL Enterprise edition and Cloud SQL Enterprise Plus edition, you can [restore backups across instances of different editions](https://docs.cloud.google.com/sql/docs/postgres/backup-recovery/restore).

## September 28, 2023

Feature

The following pg_wait_sampling and rdkit [flags](https://docs.cloud.google.com/sql/docs/postgres/flags) are generally available:

**pg_wait_sampling flags**

  * **cloudsql.enable_pg_wait_sampling:** enable the `pg_wait_sampling` extension for Cloud SQL for PostgreSQL instances.
  * **pg_wait_sampling.history_size:** set the size of the in-memory ring buffer for history sampling, in terms of the number of samples.
  * **pg_wait_sampling.history_period:** set the time interval for history sampling, in milliseconds.
  * **pg_wait_sampling.profile_period:** set the time interval for profile sampling for wait events, in milliseconds.
  * **pg_wait_sampling.profile_pid:** specify whether the wait profile that accumulates samples for each process and waits event is collected for each process or for all processes.
  * **pg_wait_sampling.profile_queries:** specify whether the wait profile is collected for each query or for all queries.



**rdkit flags**

  * **rdkit.tanimoto_threshold:** set the threshold value for the Tanimoto similarity operator.
  * **rdkit.dice_threshold:** set the threshold value for the Dice similarity operator.
  * **rdkit.do_chiral_sss:** specify whether stereochemistry is used in substructure matching.
  * **rdkit.do_enhanced_stereo_sss:** specify whether enhanced stereo is used in substructure matching.
  * **rdkit.sss_fp_size:** set the size of the fingerprint used for substructure screening, in bits.
  * **rdkit.morgan_fp_size:** set the size of morgan fingerprints, in bits.
  * **rdkit.featmorgan_fp_size:** set the size of featmorgan fingerprints, in bits.
  * **rdkit.layered_fp_size:** set the size of layered fingerprints, in bits.
  * **rdkit.rdkit_fp_size:** set the size of rdkit fingerprints, in bits.
  * **rdkit.hashed_torsion_fp_size:** set the size of topological torsion bit vector fingerprints, in bits.
  * **rdkit.hashed_atompair_fp_size:** set the size of atom pair bit vector fingerprints, in bits.
  * **rdkit.reaction_sss_fp_size:** set the size of the structural chemical reaction fingerprint, in bits.
  * **rdkit.reaction_difference_fp_size:** set the size of the difference chemical reaction fingerprint, in bits.
  * **rdkit.reaction_sss_fp_type:** specify the type of structural chemical reaction fingerprint.
  * **rdkit.reaction_difference_fp_type:** specify the type of difference chemical reaction fingerprint.
  * **rdkit.ignore_reaction_agents:** specify whether agents of a chemical reaction are taken into account.
  * **rdkit.agent_FP_bit_ratio:** specify the weight of the impact of agents contained in a chemical reaction fingerprint.
  * **rdkit.move_unmmapped_reactants_to_agents:** specify whether unmapped reactant agents of a chemical reaction are taken into account.
  * **rdkit.threshold_unmapped_reactant_atoms:** set the ratio of allowed unmapped reactant atoms.
  * **rdkit.init_reaction:** specify whether the reaction is ready for use.
  * **rdkit.difference_FP_weight_agents:** specify the weight factor for agents compared to reactants and products in reaction difference fingerprints.
  * **rdkit.difference_FP_weight_nonagents:** specify the weight factor for reactants and products compared to agents in reaction difference fingerprints.
  * **rdkit.avalon_fp_size:** set the size of avalon fingerprints, in bits.



## September 26, 2023

Feature

Cloud SQL supports the preview version of the enable-high-availability recommender. This service proactively generates recommendations that help you bring your important instances within SLA by providing data redundancy. This might be helpful during a zonal outage or when an instance runs out of memory. For more information, see [Improve instance reliability by enabling high availability](https://docs.cloud.google.com/sql/docs/postgres/recommender-enable-ha).

## September 21, 2023

Feature

The rollout of the `oracle_fdw` extension, version 1.2 is **underway**. This extension provides a foreign data wrapper for accessing Oracle databases easily and efficiently. For more information, see [Configure PostgreSQL extensions](https://docs.cloud.google.com/sql/docs/postgres/extensions).

The rollout of the following minor versions, extension versions, and plugin versions is **underway** :

**Minor versions**

  * 11.19 is upgraded to 11.21.
  * 12.14 is upgraded to 12.16.
  * 13.10 is upgraded to 13.12.
  * 14.7 is upgraded to 14.9.
  * 15.2 is upgraded to 15.4.



**Extension and plugin versions**

  * orafce is upgraded from 3.24.4 to 3.25.1.
  * pglogical is upgraded from 2.4.2 to 2.4.3.
  * pgvector is upgraded from 0.4.2 to 0.5.0.
  * PostGIS is upgraded from 3.2.3 to 3.2.5.



If you use a maintenance window, then the updates to the minor, extension, and plugin versions happen according to the timeframe that you set in the window. Otherwise, the updates occur within the next few weeks. 

The new maintenance version is `[PostgreSQL version].R20230830.01_00`. To learn how to check your maintenance version, see [Self service maintenance.](https://docs.cloud.google.com/sql/docs/postgres/self-service-maintenance#before_you_begin/self-service-maintenance) To find your maintenance window or to manage maintenance updates, see [Find and set maintenance windows](https://docs.cloud.google.com/sql/docs/postgres/set-maintenance-window).

## September 19, 2023

Feature

Support for [me-central2 (Dammam)](https://docs.cloud.google.com/sql/docs/postgres/locations) region.

## August 31, 2023

Feature

The [`pgvector`](https://docs.cloud.google.com/sql/docs/postgres/extensions) extension, version 0.4.2 is generally available. Use this extension to store and search for vector embeddings in PostgreSQL databases.

## August 28, 2023

Feature

You can now [set password policies](https://docs.cloud.google.com/sql/docs/postgres/create-manage-users#user-pwd-policy) for local database users of Cloud SQL for PostgreSQL instances.

## August 22, 2023

Feature

Support for [europe-west10 (Berlin)](https://docs.cloud.google.com/sql/docs/postgres/locations) region.

## August 21, 2023

Feature

[Private Service Connect](https://docs.cloud.google.com/sql/docs/postgres/configure-private-service-connect) is now GA for Cloud SQL for PostgreSQL. This solution allows you to connect to a Cloud SQL instance from multiple VPC networks that belong to different groups, teams, projects, or organizations.

## August 18, 2023

Feature

[Cloud SQL Enterprise Plus edition](https://docs.cloud.google.com/sql/docs/editions-intro) now supports four new regions: 

  * europe-central2 (Warsaw)
  * europe-west9 (Paris)
  * southamerica-east1 (San Paulo)
  * us-west1 (Oregon)



## August 17, 2023

Feature

You can now [re-encrypt an existing Cloud SQL CMEK-enabled primary instance or replica](https://docs.cloud.google.com/sql/docs/postgres/configure-cmek#reencrypt) with a new primary key version.

## August 11, 2023

Feature

[Cloud SQL Enterprise Plus edition](https://docs.cloud.google.com/sql/docs/postgres/editions-intro) now supports the asia-northeast3 (Seoul) region.

## August 10, 2023

Feature

You can now use point-in-time recovery to [recover a Cloud SQL instance that isn't available](https://docs.cloud.google.com/sql/docs/postgres/backup-recovery/restore#pitr-instance-not-available). If the instance is unavailable, then you can use the API to [get the latest recovery time](https://docs.cloud.google.com/sql/docs/postgres/backup-recovery/pitr#get-the-latest-recovery-time) and perform the recovery of the instance to that time.

## August 09, 2023

Feature

You can now upgrade a Cloud SQL for PostgreSQL instance to Cloud SQL Enterprise Plus edition by using [IP allowlists](https://docs.cloud.google.com/sql/docs/postgres/upgrade-cloud-sql-instance-to-enterprise-plus-ip-allowlists) and [VPC Peering](https://docs.cloud.google.com/sql/docs/postgres/upgrade-cloud-sql-instance-to-enterprise-plus-vpc-peering).

## August 03, 2023

Feature

Cloud SQL now supports multiple categories of API rate quotas. Rate quotas for each category are imposed per minute, per project, per region, and per user. For more information about rate quotas for each category, see [Quotas and limits](https://docs.cloud.google.com/sql/docs/postgres/quotas).

Feature

The [Cloud SQL Node.js Language Connector](https://docs.cloud.google.com/static/sql/docs/postgres/connect-connectors#node.js) is now available for public preview.

## July 18, 2023

Feature

Cloud SQL now supports [default maintenance windows](https://docs.cloud.google.com/sql/docs/postgres/maintenance#default-windows) for your instances. With this release, an instance without a user-specified maintenance window is maintained outside of the typical business hours for the time zone that the instance is deployed in.

## July 17, 2023

Feature

You can now [enable query insights](https://docs.cloud.google.com/sql/docs/postgres/using-query-insights#enable-insights) for multiple instances at a time.

## July 12, 2023

Feature

Cloud SQL now offers two editions of Cloud SQL to support your various business and application needs: **Cloud SQL Enterprise Plus edition** and **Cloud SQL Enterprise edition**. Each edition provides different performance and availability characteristics to meet the needs of your applications. 

Cloud SQL Editions are only available for Cloud SQL for MySQL and Cloud SQL for PostgreSQL. 

For more information about Cloud SQL editions, see [Introduction to Cloud SQL editions](https://docs.cloud.google.com/sql/docs/editions-intro).

## July 11, 2023

Feature

Cloud SQL now supports [cancelling the import and export of data](https://docs.cloud.google.com/sql/docs/postgres/import-export/cancel-import-export) into Cloud SQL for PostgreSQL instances.

## July 06, 2023

Feature

Cloud SQL now supports [non-RFC 1918 IP address ranges](https://docs.cloud.google.com/sql/docs/postgres/configure-private-ip#non-rfc1918), including privately used public IP addresses. This enables you to create instances and replicas in a non-RFC 1918 IP address range. Additionally, you can connect to an instance from an application that is running in a non-RFC 1918 IP address range.

## June 30, 2023

Feature

For our preferred partners and allowlisted customers, [Private Service Connect](https://docs.cloud.google.com/sql/docs/postgres/configure-private-service-connect) is now available. This solution allows you to connect to a Cloud SQL instance from multiple VPC networks that belong to different groups, teams, projects, or organizations. To use Private Service Connect, contact your Technical Account Manager.

## June 15, 2023

Feature

The [Cloud SQL System insights dashboard](https://docs.cloud.google.com/sql/docs/postgres/use-system-insights) is now generally available and includes more [metrics](https://docs.cloud.google.com/sql/docs/postgres/admin-api/metrics). You can also use the **Customize dashboard** option to personalize the dashboard and choose the metrics you want to see on it.

## June 02, 2023

Feature

The rollout of the following minor versions, extension versions, and plugin versions is currently underway:

**Minor versions**

  * 10.22 is upgraded to 10.23.
  * 11.17 is upgraded to 11.19.
  * 12.12 is upgraded to 12.14.
  * 13.8 is upgraded to 13.10.
  * 14.5 is upgraded to 14.7.



**Extension and plugin versions**

  * pg_cron is upgraded from 1.4.1 to 1.5.
  * pg_partman is upgraded from 4.7.0 to 4.7.3.
  * postgresql-hll is upgraded from 2.16 to 2.17.
  * pg_repack is upgraded from 1.4.7 to 1.4.8.
  * wal2json is upgraded from 2.4 to 2.5.
  * pg_hint_plan is upgraded, as follows: 
    * from 1.3.7 to 1.3.8 (for PostgreSQL versions 11-13)
    * from 1.4.0 to 1.4.1 (for PostgreSQL version 14)
    * from 1.4.0 to 1.5.0 (for PostgreSQL version 15)



If you use a maintenance window, then the updates to the minor, extension, and plugin versions happen according to the timeframe that you set in the window. Otherwise, the updates occur within the next few weeks. 

The new maintenance version is `[PostgreSQL version].R20230530.01_00`. To learn how to check your maintenance version, see [Self service maintenance.](https://docs.cloud.google.com/sql/docs/postgres/self-service-maintenance#before_you_begin/self-service-maintenance) To find your maintenance window or to manage maintenance updates, see [Find and set maintenance windows](https://docs.cloud.google.com/sql/docs/postgres/set-maintenance-window).

## May 24, 2023

Feature

PostgreSQL version 15 is now generally available. To start using PostgreSQL 15, see [Create instances](https://docs.cloud.google.com/sql/docs/postgres/create-instance).

## May 19, 2023

Feature

The following [extensions](https://docs.cloud.google.com/sql/docs/postgres/extensions), [views](https://docs.cloud.google.com/sql/docs/postgres/users#pg_shadow), [utilities](https://docs.cloud.google.com/sql/docs/postgres/import-export/import-export-dmp), and [flags](https://docs.cloud.google.com/sql/docs/postgres/flags) are generally available:

**Extensions**

  * **postgresql_anonymizer:** mask or replace personally identifiable information (PII) or sensitive data from a PostgreSQL database.
  * **pgtt:** create, manage and use Oracle-style global temporary tables.
  * **rdkit:** compare, manipulate, and identify molecular structures.



**Views and utilities**

  * **pg_authid:** access this catalog table that contains hashed passwords and other properties for all database roles.
  * **pg_dumpall:** extract all PostgreSQL databases of a cluster into a single script file.



**Flags**

  * **log_line_prefix:** generate a printf-style string at the beginning of each line of a PostgreSQL log file.



The rollout of the following minor versions, extension versions, and plugin versions is currently underway:

**Minor versions**

  * 10.21 is upgraded to 10.22.
  * 11.16 is upgraded to 11.17.
  * 12.11 is upgraded to 12.12.
  * 13.7 is upgraded to 13.8.
  * 14.4 is upgraded to 14.5.



**Extension and plugin versions**

  * plv8 is upgraded from 3.1.2 to 3.1.4.
  * wal2json is upgraded from 2.3 to 2.4.
  * pgTAP is upgraded from 1.1.0 to 1.2.0.
  * PostGIS is upgraded from 3.1.4 to 3.1.7.
  * pg_partman is upgraded from 4.5.1 to 4.7.0.
  * pg_wait_sampling is upgraded from 1.1.3 to 1.1.4.
  * pg_hint_plan is upgraded from 1.3.7 to 1.4.
  * pglogical is upgraded from 2.4.1 to 2.4.2.



This rollout also introduces the following:

  * PostGIS GDAL driver support
  * LZ4 TOAST compression for PostgreSQL versions 14 and later



## May 16, 2023

Feature

The Cloud SQL Proxy Operator is now generally available. To learn more about the Cloud SQL Proxy Operator, see [About the Cloud SQL Proxy Operator](https://docs.cloud.google.com/sql/docs/mysql/connect-proxy-operator).

## May 02, 2023

Feature

[Fast migration for Cloud SQL](https://docs.cloud.google.com/sql/docs/postgres/faq#data-migration) is now available. This feature improves the performance of data migrations from an external source to a destination Cloud SQL instance.

## April 15, 2023

Announcement

The changes listed in the [March 29th](https://docs.cloud.google.com/sql/docs/postgres/release-notes#March_29_2023) release notes entry for PostgreSQL minor versions, extension versions, and plugin versions have been postponed.

## April 06, 2023

Feature

Cascading Replicas is now generally available when migrating from external servers. You can now configure migrated replicas to have read replicas under them before promoting them to primary replica. To learn more, see [External Server Cascading Replicas](https://docs.cloud.google.com/sql/docs/postgres/replication/external-server#es-cascading-replicas).

## March 30, 2023

Feature

Support for [me-central1](https://docs.cloud.google.com/sql/docs/mysql/locations) (Doha) region.

## March 29, 2023

Feature

The rollout of the following PostgreSQL minor versions, extension versions, and plugin versions is currently underway:

**Minor versions**

  * 10.21 is upgraded to 10.22.
  * 11.16 is upgraded to 11.17.
  * 12.11 is upgraded to 12.12.
  * 13.7 is upgraded to 13.8.
  * 14.4 is upgraded to 14.5.



**Extension and plugin versions**

  * plv8 is upgraded from 3.1.2 to 3.1.4.
  * wal2json is upgraded from 2.3 to 2.4.
  * pgTAP is upgraded from 1.1.0 to 1.2.0.
  * PostGIS is upgraded from 3.1.4 to 3.1.7.
  * pg_partman is upgraded from 4.5.1 to 4.7.0.
  * pg_wait_sampling is upgraded from 1.1.3 to 1.1.4.
  * pg_hint_plan is upgraded from 1.3.7 to 1.4.
  * pglogical is upgraded from 2.4.1 to 2.4.2.



If you use a maintenance window, then the updates to the minor, extension, and plugin versions happen according to the timeframe that you set in the window. Otherwise, the updates occur within the next few weeks. 

The new maintenance version is `[PostgreSQL version].R20230316.02_02`. To learn how to check your maintenance version, see [Self service maintenance.](https://docs.cloud.google.com/sql/docs/postgres/self-service-maintenance#before_you_begin/self-service-maintenance) To find your maintenance window or to manage maintenance updates, see [Find and set maintenance windows](https://docs.cloud.google.com/sql/docs/postgres/set-maintenance-window).

## March 28, 2023

Feature

The changes in the September 15, 2022 Release Notes entry for read replica maintenance are now available. Cloud SQL read replicas follow the [maintenance settings](https://docs.cloud.google.com/sql/docs/postgres/maintenance#management) for the primary instance, including the maintenance window, rescheduling, and the deny maintenance period. During the maintenance event, Cloud SQL maintains the replicas before maintaining the primary instance. For more information, see [How does maintenance affect read replicas?](https://docs.cloud.google.com/sql/docs/postgres/maintenance#read-replicas)

## March 23, 2023

Feature

Support for [europe-west12](https://docs.cloud.google.com/sql/docs/mysql/locations) (Turin) region.

## March 21, 2023

Feature

Smaller read replicas are now available for Cloud SQL. Read replicas no longer require the same or more CPUs and RAM than their primary instances.

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

Cloud SQL supports the preview version of the [Underprovisioned instance recommender](https://docs.cloud.google.com/sql/docs/postgres/recommender-underprovisioned). This service helps you avoid bottlenecks from high CPU and memory usage and minimize the likelihood of out-of-memory events. It gives you recommendations to resize your instances to a machine tier that better suits your workload.

## January 18, 2023

Feature

Cloud SQL now supports [viewing an audit log for an automated backup of an instance](https://docs.cloud.google.com/sql/docs/postgres/backup-recovery/view-audit-logs-for-automated-backups) to verify whether the backup is completed successfully. You can also configure a log-based alert so that a user can be notified of the backup's status.

## January 09, 2023

Feature

For new Cloud SQL instances that have [point-in-time recovery](https://docs.cloud.google.com/sql/docs/postgres/backup-recovery/restore#tips-pitr) enabled or for existing instances that enable point-in-time recovery, Cloud SQL for PostgreSQL now stores write-ahead logs in Google Cloud Storage. 

Before this release, write-ahead logs, which are used to perform point-in-time recovery, were stored on disk. Now, logs are stored in Google Cloud Storage in the same region as the instances. 

All other existing instances that have point-in-time recovery enabled will continue to have their logs stored on disk. The change to storing logs in Google Cloud Storage will be made available at a later time.

## December 15, 2022

Feature

You can now allow other Google Cloud services, such as BigQuery, to access data in Cloud SQL for PostgreSQL and make queries against this data over a private connection. For more information, see [Create instances](https://docs.cloud.google.com/sql/docs/postgres/create-instance).

## December 13, 2022

Feature

The Cloud SQL [System insights dashboard](https://docs.cloud.google.com/sql/docs/postgres/use-system-insights) now shows additional metrics and an events timeline. You can also use the **Auto refresh** function to keep the dashboard up to date.

## December 01, 2022

Announcement

The changes listed in the [October 19th](https://docs.cloud.google.com/sql/docs/postgres/release-notes#October_19_2022) release notes entry for PostgreSQL minor versions, extension versions, and plugin versions have been postponed.

## October 28, 2022

Change

The changes listed in the [September 15 Release Notes entry](https://docs.cloud.google.com/sql/docs/release-notes#September_15_2022) for read replica maintenance have been postponed.

## October 19, 2022

Feature

The rollout of the following PostgreSQL minor versions, extension versions, and plugin versions is currently underway:

**Minor versions**

  * 10.21 is upgraded to 10.22.
  * 11.16 is upgraded to 11.17.
  * 12.11 is upgraded to 12.12.
  * 13.7 is upgraded to 13.8.
  * 14.4 is upgraded to 14.5.



**Extension and plugin versions**

  * plv8 is upgraded from 3.1.2 to 3.1.4.
  * wal2json is upgraded from 2.3 to 2.4.
  * pgTAP is upgraded from 1.1.0 to 1.2.0.
  * PostGIS is upgraded from 3.1.4 to 3.1.7.



In addition, this rollout introduces the following changes to collation support:

  1. The `C.UTF-8` collation is renamed to `C.utf8`. The original name is supported as an alias of the new name.
  2. The following collations aren't supported anymore:

     * `as_IN.utf8`
     * `az_AZ.utf8`
     * `ca_ES.utf8@valencia`
     * `eo.utf8`
     * `ia`
     * `iw_IL`
     * `iw_IL.utf8`
     * `pap_AN`
     * `tt_RU.utf8`
     * `tt_RU.utf8@iqtelif`



If you use a maintenance window, then the updates to the minor, extension, and plugin versions happen according to the timeframe that you set in the window. Otherwise, the updates occur within the next few weeks. 

The new maintenance version is `[PostgreSQL version].R20221017.01_00`. To learn how to check your maintenance version, see [Self service maintenance.](https://docs.cloud.google.com/sql/docs/postgres/self-service-maintenance#before_you_begin/self-service-maintenance) To find your maintenance window or to manage maintenance updates, see [Find and set maintenance windows](https://docs.cloud.google.com/sql/docs/postgres/set-maintenance-window).

## October 11, 2022

Feature

Cloud SQL supports the preview version of the [high transaction ID utilization recommender](https://docs.cloud.google.com/sql/docs/postgres/recommender-high-transactionid-utilization) that helps you avoid potential transaction ID wraparound for Cloud SQL for PostgreSQL instances.

## October 05, 2022

Feature

Cloud SQL for PostgreSQL now supports the `log_timezone` and `TimeZone` flags. For more information, see the [Configure database flags](https://cloud.google.com/sql/docs/postgres/flags) page.

## October 04, 2022

Feature

Terraform is supported when you use [self-service maintenance](https://docs.cloud.google.com/sql/docs/mysql/self-service-maintenance#update-maintenance-version).

## September 30, 2022

Feature

Cloud SQL for PostgreSQL supports in-place major version upgrades in GA. You can upgrade your instance's major version to a more recent version. For more information, see [Upgrade the database major version in-place](https://docs.cloud.google.com/sql/docs/postgres/upgrade-major-db-version-inplace).

## September 21, 2022

Feature

Cloud SQL allows the re-use of an instance name immediately after the instance is deleted. For more information, see the [Cloud SQL for PostgreSQL FAQ](https://docs.cloud.google.com/sql/docs/postgres/faq#reuse).

## September 15, 2022

Feature

Cloud SQL read replicas now follow the [maintenance settings](https://docs.cloud.google.com/sql/docs/postgres/maintenance#management) for the primary instance, including the maintenance window, rescheduling, and the deny maintenance period. During the maintenance event, Cloud SQL maintains the replicas before maintaining the primary instance. For more information, see [How does maintenance affect read replicas?](https://docs.cloud.google.com/sql/docs/postgres/maintenance#read-replicas)

## September 13, 2022

Feature

Support for me-west1 (Tel Aviv).

## September 12, 2022

Feature

[Cascading Replicas](https://docs.cloud.google.com/sql/docs/postgres/replication#cascading-replicas) is now generally available for Cloud SQL. Customers can now configure PostgreSQL and MySQL for Cloud SQL read replicas to have read replicas under them.

## August 26, 2022

Feature

The following extensions in Cloud SQL for PostgreSQL are [generally available](https://docs.cloud.google.com/sql/docs/postgres/extensions): 

  * **pgRouting.** Enhances geospatial processing, through network routing and analysis, for PostGIS.
  * **plv8.** Provides a procedural language for enabling the use of JavaScript.
  * **amcheck.** Enables the use of the pg_amcheck application to check for corruption in PostgreSQL databases.



## August 15, 2022

Feature

By enabling instance deletion protection, you can prevent the accidental removal of Cloud SQL instances. This functionality is generally available.

For more information, see [Prevent deletion of an instance](https://docs.cloud.google.com/sql/docs/mysql/deletion-protection).

## August 05, 2022

Feature

The new Cloud SQL [System insights dashboard](https://docs.cloud.google.com/sql/docs/postgres/use-system-insights) helps you detect and analyze system performance problems.

## July 29, 2022

Change

For PostgreSQL versions 9.6 to 13, the `[PostgreSQL version].R20220710.01_00` maintenance version caused a behavior change for configuration parameters: Session-level configuration parameters with dashes (`-`) cannot be set. 

After you [check your current maintenance version](https://docs.cloud.google.com/sql/docs/postgres/self-service-maintenance#before_you_begin), you can apply a fix by performing a [self-service maintenance](https://docs.cloud.google.com/sql/docs/postgres/self-service-maintenance) update to the latest release.

Please use this table to find the name of the maintenance version to apply, and use that version or the latest version available:

PostgreSQL version | Maintenance version  
---|---  
PostgreSQL 9.6 | POSTGRES_9_6_24.R20220710.01_02  
PostgreSQL 10 | POSTGRES_10_21.R20220710.01_02  
PostgreSQL 11 | POSTGRES_11_16.R20220710.01_02  
PostgreSQL 12 | POSTGRES_12_11.R20220710.01_02  
PostgreSQL 13 | POSTGRES_13_7.R20220710.01_02  
  
After you have identified the name of the maintenance version, please [upgrade to the target maintenance version](https://docs.cloud.google.com/sql/docs/postgres/self-service-maintenance#update-maintenance-version), performing the corresponding update of your instances (to the latest maintenance version). 

Note that newly created instances automatically use the latest version.

## July 25, 2022

Feature

The following PostgreSQL minor versions and extension versions are now available: 

  * 14.3 is upgraded to 14.4.
  * 13.6 is upgraded to 13.7.
  * 12.10 is upgraded to 12.11.
  * 11.15 is upgraded to 11.16.
  * 10.20 is upgraded to 10.21.



If you use maintenance windows, then you might not yet have these versions. In this case, you'll see the new versions after your maintenance update occurs. To find your maintenance window or to manage maintenance updates, see [Find and set maintenance windows](https://docs.cloud.google.com/sql/docs/postgres/set-maintenance-window).

Feature

Added information about checking the `LC_COLLATE` value for your databases before performing a major version upgrade of the databases for your Cloud SQL for PostgreSQL instance. For more information, refer to the [Cloud SQL](https://cloud.google.com/sql/docs/postgres/upgrade-major-db-version-inplace#prepare_for_a_major_version_upgrade) documentation.

## July 11, 2022

Feature

You can enable [high availability](https://docs.cloud.google.com/sql/docs/mysql/configure-ha#ha-existing) for read replicas. See [Disaster recovery](https://docs.cloud.google.com/sql/docs/mysql/replication/cross-region-replicas#disaster_recovery) for additional information about the use of high-availability replicas in a disaster recovery configuration.

Feature

You can create [external server replicas with HA](https://docs.cloud.google.com/sql/docs/mysql/replication/configure-replication-from-external#setup-replica-instance) enabled.

## July 08, 2022

Feature

The July maintenance changelog is now available. For more information, use the links at [Maintenance changelog](https://docs.cloud.google.com/sql/docs/postgres/maintenance-changelog).

## June 28, 2022

Feature

A second June maintenance changelog is now available. For more information, use the links at [Maintenance changelog](https://docs.cloud.google.com/sql/docs/postgres/maintenance-changelog).

The fix to the silent data corruption when using the CREATE INDEX CONCURRENTLY or REINDEX CONCURRENTLY SQL commands in PostgreSQL 14 ([BUG #17485](https://www.postgresql.org/message-id/17485-396609c6925b982d%40postgresql.org)) is now available in the self-service maintenance release POSTGRES_14_2.R20220331.02_012 for PostgreSQL 14.2. 

After applying the [self service maintenance](https://docs.cloud.google.com/sql/docs/postgres/self-service-maintenance), you can fix any silent data corruption if it already happens using REINDEX CONCURRENTLY SQL command on the specific indexes, or reindexdb client command for your entire instance.

## June 23, 2022

Feature

Cloud SQL for PostgreSQL now supports [replication from an external server](https://docs.cloud.google.com/sql/docs/postgres/replication/configure-replication-from-external).

## June 14, 2022

Feature

For enhanced security with built-in authentication, Cloud SQL now lets you set [password policies](https://docs.cloud.google.com/sql/docs/postgres/built-in-authentication) at the instance level.

## June 13, 2022

Feature

The following extensions in Cloud SQL for PostgreSQL are [generally available](https://docs.cloud.google.com/sql/docs/postgres/extensions#miscellaneous-extensions): 

  * **pg_bigm.** Enables full text search and allows a two-gram (bigram) index for faster full text search.
  * **refint.** Enables the checking of foreign key restraints, the referencing table, and the referenced table.
  * **decoderbufs.** A logical decoder that delivers output data as Protocol Buffers, adapted for Debezium.
  * **pg_wait_sample**. Collects sampling statistics of wait events, providing wait event data for processes on servers.



Additionally, users with the `cloudsqlsuperuser` role have full access to the `pg_largeobject` system catalog.

Feature

Cloud SQL enables you to access to the `pg_shadow` view. You can use the `[pg_shadow](https://www.postgresql.org/docs/current/static/view-pg-shadow.html)` view to work with the properties of roles that are marked as `rolcanlogin` in the `[pg_authid](https://www.postgresql.org/docs/current/static/catalog-pg-authid.html)` catalog.

For more information, see [Access to the pg_shadow view](https://docs.cloud.google.com/sql/docs/postgres/users#pg_shadow).

## June 10, 2022

Feature

Cloud SQL now supports faster machine type changes, with connectivity dropping to less than 60 seconds. For more information, see [Impact of changing instance settings](https://docs.cloud.google.com/sql/docs/postgres/instance-settings#impact).

## June 09, 2022

Feature

The June maintenance changelog is now available. For more information, use the links at [Maintenance changelog](https://docs.cloud.google.com/sql/docs/postgres/maintenance-changelog).

## June 08, 2022

Feature

An addendum to the May maintenance changelog shows additional security patches. For more information, use the links at [Maintenance changelog](https://docs.cloud.google.com/sql/docs/postgres/maintenance-changelog).

Feature

New maintenance versions are now available through [self-service maintenance](https://docs.cloud.google.com/sql/docs/postgres/self-service-maintenance). See the [maintenance changelog](https://docs.cloud.google.com/sql/docs/postgres/maintenance-changelog) to learn more about these new maintenance versions.

## June 07, 2022

Feature

Support for us-south1 (Dallas).

## May 24, 2022

Feature

Support for us-east5 (Columbus).

## May 04, 2022

Feature

Support for europe-west9 (Paris).

## May 02, 2022

Feature

New maintenance versions are now available through [self-service maintenance](https://docs.cloud.google.com/sql/docs/postgres/self-service-maintenance). See the [maintenance changelog](https://docs.cloud.google.com/sql/docs/postgres/maintenance-changelog) to learn more about these new maintenance versions.

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

Feature

The following PostgreSQL minor versions and extension versions are now available. If you use maintenance windows, you might not yet have these versions. In this case, you will see the new versions after your maintenance update occurs. To find your maintenance window or manage maintenance updates, see [Finding and setting maintenance windows](https://docs.cloud.google.com/sql/docs/postgres/set-maintenance-window). 

  * 14.1 is upgraded to 14.2.
  * 13.5 is upgraded to 13.6.
  * 12.9 is upgraded to 12.10.
  * 11.14 is upgraded to 11.15.
  * 10.19 is upgraded to 10.20.



## April 20, 2022

Feature

Support for europe-west8 region (Milan).

## April 12, 2022

Feature

Customer-managed encryption key (CMEK) organization policy constraints are now available in [Preview](https://cloud.google.com/products/#product-launch-stages).

  * `constraints/gcp.restrictNonCmekServices` allows you to control which resources require the use of CMEK.
  * `constraints/gcp.restrictCmekCryptoKeyProjects` allows you to control the projects from which a Cloud KMS key can be used to validate requests.



You can use both constraints together to enforce the use of CMEK from allowed projects. 

To learn more, see [Customer-managed encryption keys (CMEK) organization policies](https://docs.cloud.google.com/sql/docs/mysql/org-policy/org-policy#customer-managed_encryption_keys_cmek_organization_policies). To add CMEK organization policies now, see [Add Cloud SQL organization policies](https://docs.cloud.google.com/sql/docs/mysql/org-policy/configure-org-policy).

## April 11, 2022

Feature

Cloud SQL for PostgreSQL supports in-place major version upgrades in Preview. You can upgrade your instance's major version to a more recent version. For more information, see [Upgrade the database major version in-place](https://docs.cloud.google.com/sql/docs/postgres/upgrade-major-db-version-inplace).

## February 24, 2022

Change

Due to a change in a recent maintenance update, the changes listed in the [February 4 Release Notes entry](https://docs.cloud.google.com/sql/docs/postgres/release-notes#February_04_2022) have been applied to some instances but postponed for the others. In the Google Cloud Console, you can determine if the maintenance update was applied. Specifically, on the [Instance Overview page](https://docs.cloud.google.com/sql/docs/postgres/instance-info#info), review the instance's [operations and logs](https://docs.cloud.google.com/sql/docs/postgres/instance-info#operations_and_logs) for an occurrence of a maintenance operation since January 27.

## February 23, 2022

Feature

If your primary instance uses a private IP address, you can now select an allocated IP range for [clones](https://docs.cloud.google.com/sql/docs/postgres/clone-instance#cloning-an-instance-with-a-private-ip) and [replicas](https://docs.cloud.google.com/sql/docs/postgres/replication/create-replica#gcloud) created from the instance.

## February 17, 2022

Feature

Cloud SQL now supports the use of tags on instances. Tags are key-value pairs you can apply to your resources, such as a project or a Cloud SQL instance, which are used for fine-grained access control. To learn more, see [Access control with Google Cloud tags](https://docs.cloud.google.com/sql/docs/mysql/tags). To use tags now, see [Attach and manage tags on Cloud SQL instances](https://docs.cloud.google.com/sql/docs/mysql/manage-tags).

## February 08, 2022

Feature

Cloud SQL supports the [`max_parallel_maintenance_workers`](https://www.postgresql.org/docs/current/static/runtime-config-resource.html#GUC-MAX-PARALLEL-MAINTENANCE-WORKERS), [`max_parallel_workers`](https://www.postgresql.org/docs/current/static/runtime-config-resource.html#GUC-MAX-PARALLEL-WORKERS),  
[`max_parallel_workers_per_gather`](https://www.postgresql.org/docs/current/static/runtime-config-resource.html#GUC-MAX-PARALLEL-WORKERS-PER-GATHER), and [`max_pred_locks_per_transaction`](https://www.postgresql.org/docs/current/static/runtime-config-locks.html#GUC-MAX-PRED-LOCKS-PER-TRANSACTION) flags: 

  * `max_parallel_maintenance_workers` sets the maximum number of parallel workers that can be started by a single utility command.
  * `max_parallel_workers` sets the maximum number of workers that the system can support for parallel operations.
  * `max_parallel_workers_per_gather` sets the maximum number of workers that can be started by a single Gather or Gather Merge node.
  * `max_pred_locks_per_transaction` controls the average number of object locks allocated for each transaction.



For more information, see [Supported flags](https://docs.cloud.google.com/sql/docs/postgres/flags#postgres-m).

## February 07, 2022

Feature

Cloud SQL supports the [`wal_receiver_timeout`](https://www.postgresql.org/docs/current/static/runtime-config-replication.html#GUC-WAL-RECEIVER-TIMEOUT) and [`wal_sender_timeout`](https://www.postgresql.org/docs/current/static/runtime-config-replication.html#GUC-WAL-SENDER-TIMEOUT) flags: 

  * The `wal_receiver_timeout` flag ends replication connections that are inactive for the specified time.
  * The `wal_sender_timeout` flag, which is for detection by the ending server, ends replication connections that are inactive for the specified time.



For more information, see [Supported flags](https://docs.cloud.google.com/sql/docs/postgres/flags#postgres-w).

## February 04, 2022

Feature

The following PostgreSQL minor versions and extension versions are now available. If you use maintenance windows, you might not yet have these versions. In this case, you will see the new versions after your maintenance update occurs. To find your maintenance window or manage maintenance updates, see [Finding and setting maintenance windows](https://docs.cloud.google.com/sql/docs/postgres/set-maintenance-window). 

  * 14.0 is upgraded to 14.1. 
  * 13.4 is upgraded to 13.5. 
  * 12.8 is upgraded to 12.9. 
  * 11.13 is upgraded to 11.14. 
  * 10.18 is upgraded to 10.19. 
  * 9.6.23 is upgraded to 9.6.24. 



Additionally, the following extensions have been upgraded. For more information about these and other extensions, see [PostgreSQL extensions](https://docs.cloud.google.com/sql/docs/postgres/extensions).

  * The pglogical extension is upgraded to 2.4.1. 
  * The pgaudit extension is upgraded as follows: 

    * For PostgreSQL 14, upgraded to 1.6.1. 
    * For PostgreSQL 13, upgraded to 1.5.1. 
    * For PostgreSQL 12, upgraded to 1.4.2. 
    * For PostgreSQL 11, upgraded to 1.3.3. 
    * For PostgreSQL 10, upgraded to 1.2.3. 
    * For PostgreSQL 9.6, upgraded to 1.1.4.



## February 01, 2022

Feature

Query Insights lets you configure the query sampling rate. For information, see [Using Query Insights to improve query performance](https://docs.cloud.google.com/sql/docs/postgres/using-query-insights).

## January 31, 2022

Feature

The Key Access Justifications (KAJ) feature is now generally available in Cloud SQL. You can use KAJ as part of [Cloud External Key Manager (EKM)](https://docs.cloud.google.com/kms/docs/ekm). KAJ enables you to view the reason for each Cloud EKM request. Additionally, based on the justification provided, you can automatically approve or deny a request. For related information, see the [Overview](https://docs.cloud.google.com/cloud-provider-access-management/key-access-justifications/docs/overview).

## December 16, 2021

Feature

You can now see the database minor version when viewing information about an instance. See [Database versions and version policies](https://docs.cloud.google.com/sql/docs/sqlserver/db-versions) for a list of the latest supported versions.

## December 15, 2021

Feature

PostgreSQL version 14 is now generally available. To start using PostgreSQL 14, see [Create instances](https://docs.cloud.google.com/sql/docs/postgres/create-instance).

## December 09, 2021

Feature

Cloud SQL now limits the rate for backup and restore operations on the data disk. For more information, see [Backup rate limitations](https://docs.cloud.google.com/sql/docs/postgres/backup-recovery/backups#backup_rate_limitations) and [Restore rate limitations](https://docs.cloud.google.com/sql/docs/postgres/backup-recovery/restore#restore_rate_limitations).

## November 19, 2021

Feature

The following extensions in Cloud SQL for PostgreSQL are [generally available](https://docs.cloud.google.com/sql/docs/postgres/extensions#miscellaneous-extensions): 

  * **auto_explain.** Enables you to automatically log execution plans of slow statements, for troubleshooting and more. Provides an automated way to perform the functionality of the [EXPLAIN](https://www.postgresql.org/docs/9.1/sql-explain.html) command.
  * **pg_cron.** A cron-based job scheduler, this extension enables cron syntax to schedule commands from a database.
  * **pg_hint_plan.** Enables you to improve PostgreSQL execution plans using hints, which are simple descriptions in SQL comments.
  * **pg_proctab.** Enables you to use [pg_top](https://pg_top.gitlab.io/) with Cloud SQL for PostgreSQL, and generate reports from the operating system process table.



## November 16, 2021

Feature

Support for [southamerica-west1](https://docs.cloud.google.com/sql/docs/mysql/locations#location-r) (Santiago) region.

## October 29, 2021

Feature

  * The following PostgreSQL minor versions and extension versions are now available. If you use maintenance windows, you might not yet have these versions. In this case, you will see the new versions after your maintenance update occurs. To find your maintenance window or manage maintenance updates, see [Finding and setting maintenance windows](https://docs.cloud.google.com/sql/docs/postgres/set-maintenance-window). 
    * 9.6.22 is upgraded to 9.6.23.
    * 10.17 is upgraded to 10.18.
    * 11.12 is upgraded to 11.13.
    * 12.7 is upgraded to 12.8.
    * 13.3 is upgraded to 13.4.
  * The hll extension is upgraded to 2.16.
  * The pglogical extension is upgraded to 2.4.0.
  * The pg_partman extension is upgraded to 4.5.1.
  * The pg_repack extension is upgraded to 1.4.7.



## October 26, 2021

Feature

Cloud SQL now supports the max_pred_locks_per_page and max_pred_locks_per_relation flags. For information about the Cloud SQL implementation of these flags, see [Supported flags](https://sql/docs/postgres/flags#postgres-m).

## October 08, 2021

Feature

Access Approval is now GA for Cloud SQL. Access Approval enables you to require explicit approval before Google Support may access your database for support purposes.To learn about access approval, see [Overview of Access Approval](https://docs.cloud.google.com/cloud-provider-access-management/access-approval/docs/overview). To set up access approval now, see the [Access Approval Quickstart](https://docs.cloud.google.com/cloud-provider-access-management/access-approval/docs/quickstart).

## September 28, 2021

Feature

Cloud SQL supports the preview version of two recommenders that help you optimize your database costs:

  * [Idle database instance recommender](https://docs.cloud.google.com/sql/docs/mysql/recommender-sql-idle): Identifies idle database instances in your project and provides recommendations about the savings that you can make by shutting them down. 

  * [Overprovisioned database instance recommender](https://docs.cloud.google.com/sql/docs/mysql/recommender-sql-overprovisioned): Identifies overprovisioned database instances in your project and provides recommendations about the savings that you can make by rightsizing these instances.




Feature

When a database instance is nearly out of storage capacity, it's automatically stopped to prevent the loss of information. For more information, see [Stopping an instance](https://docs.cloud.google.com/sql/docs/mysql/start-stop-restart-instance#stop).

## September 14, 2021

Feature

Cloud SQL for PostgreSQL has enhanced the support for multiline log entries in `postgres.log`. Before, when a log entry spanned multiple lines, each line was recorded as a separate entry in Cloud Logging. The lines are now recorded as a single entry in Cloud Logging for ease of query and processing.

Feature

Cloud SQL for PostgreSQL now supports custom formatting controls for CSVs. For more information on how to select custom characters for field delimiters, quotes, escapes, and other characters in admin exports and imports, see [our documentation](https://docs.cloud.google.com/sql/docs/postgres/import-export/import-export-csv).

## September 10, 2021

Feature

The Cloud SQL [out-of-disk recommender](https://docs.cloud.google.com/sql/docs/mysql/using-ood-recommender) is now generally available. This feature proactively generates recommendations that help you reduce the risk of downtime that might be caused by your instances running out of disk space.

Feature

Cloud SQL for PostgreSQL now supports the `min_wal_size` flag. For more information about this flag, see the [Cloud SQL for PostgreSQL flags](https://docs.cloud.google.com/sql/docs/postgres/flags#postgres-m) documentation.

## August 30, 2021

Feature

Cloud SQL for PostgreSQL support for pglogical, native logical replication, and change data capture (CDC) using wal2json and test_decoding is now generally available.

Feature

Cloud SQL for PostgreSQL support for Automatic IAM database authentication is now generally available. See [Automatic IAM database authentication](https://docs.cloud.google.com/sql/docs/postgres/authentication#automatic).

## August 27, 2021

Feature

Cloud SQL for PostgreSQL now supports the following flags:

  * huge_pages
  * shared_buffers
  * wal_buffers



For more information about these flags, see the [Cloud SQL for PostgreSQL flags](https://docs.cloud.google.com/sql/docs/postgres/flags) documentation.

## August 21, 2021

Feature

Cloud SQL now supports [IAM Conditions](https://docs.cloud.google.com/sql/docs/mysql/project-access-control#iam-conditions). 

You can use IAM Conditions to define and enforce conditional, attribute-based access control for Google Cloud resources, including Cloud SQL instances. See [Overview of IAM Conditions](https://docs.cloud.google.com/iam/docs/conditions-overview) for more information.

## August 17, 2021

Feature

Cloud SQL now offers [faster maintenance](https://docs.cloud.google.com/sql/docs/postgres/maintenance#how_long_does_maintenance_take), with connectivity dropping for less than 30 seconds on average.

## August 09, 2021

Feature

The Cloud SQL Admin API v1 is now generally available. It is and will continue to be compatible with the v1beta4 version. There is no requirement to migrate from v1beta4 to the v1 Admin API.

## August 03, 2021

Feature

Support for [northamerica-northeast2-a,b,c](https://docs.cloud.google.com/sql/docs/mysql/locations#location-r) (Toronto) region.

## July 29, 2021

Feature

  * Cloud SQL for PostgreSQL now supports the following flags: 
    * tcp_keepalives_count
    * tcp_keepalives_idle
    * tcp_keepalives_interval



For more information about these flags, see the [Cloud SQL for PostgreSQL flags](https://docs.cloud.google.com/sql/docs/postgres/flags#postgres-t) documentation.

## July 26, 2021

Feature

  * The following PostgreSQL minor versions and extension versions are now available. If you use maintenance windows, you might not yet have these versions. In this case, you will see the new versions once your maintenance update occurs. To find your maintenance window or manage maintenance updates, see [Finding and setting maintenance windows](https://docs.cloud.google.com/sql/docs/postgres/set-maintenance-window). 
    * 9.6.21 is upgraded to 9.6.22.
    * 10.16 is upgraded to 10.17.
    * 11.11 is upgraded to 11.12.
    * 12.6 is upgraded to 12.7.
    * 13.2 is upgraded to 13.3.
  * pglogical extension is upgraded to 2.3.4.
  * PostGIS extension is upgraded to 3.0.3 for all PostgreSQL major versions.



## June 29, 2021

Feature

Support for [asia-south2](https://docs.cloud.google.com/sql/docs/mysql/locations#location-r) (Delhi) region.

## June 23, 2021

Feature

Cloud SQL storage limits are now increased to support up to 64 TB. See [Cloud SQL storage limits](https://docs.cloud.google.com/sql/docs/quotas#storage_limits) for more information.

## June 21, 2021

Feature

Support for [australia-southeast2](https://docs.cloud.google.com/sql/docs/mysql/locations#location-r) (Melbourne) region.

## June 17, 2021

Feature

[Query Insights](https://docs.cloud.google.com/sql/docs/postgres/using-query-insights) is now supported for read replicas.

## June 07, 2021

Feature

Cloud SQL now offers [faster maintenance](https://docs.cloud.google.com/sql/docs/postgres/maintenance#how_long_does_maintenance_take), with connectivity dropping for less than 60 seconds on average.

## June 04, 2021

Feature

Both the [Cloud SQL Java Connector](https://github.com/GoogleCloudPlatform/cloud-sql-jdbc-socket-factory) and [Cloud SQL Python Connector](https://github.com/GoogleCloudPlatform/cloud-sql-python-connector) now support IAM Authentication for PostgreSQL.

## June 01, 2021

Feature

The logical replication and decoding functionality of PostgreSQL is available as a preview. These features enable logical replication workflows and change data capture workflows.

For more information, see [Setting up logical replication and decoding](https://docs.cloud.google.com/sql/docs/postgres/replication/configure-logical-replication).

Feature

Cloud SQL for PostgreSQL now supports the [pg_similarity](https://docs.cloud.google.com/sql/docs/postgres/extensions#miscellaneous-extensions) extension, which provides support for similarity queries in PostgreSQL.

Also, the default value for the database flag `autovacuum_vacuum_cost_delay` is changed to 2 milliseconds in PostgreSQL 9.6, 10 and 11.

The minor versions for various extensions have also been upgraded:

| 9.6 | 10 | 11 | 12 | 13  
---|---|---|---|---|---  
address_standardizer | not avail | 2.4.9 | 2.5.5 | 3.0.2 | 3.0.2  
hll | 2.14 | 2.14 | 2.14 | 2.14 | 2.14  
pg_repack | 1.4.6 | 1.4.6 | 1.4.6 | 1.4.6 | 1.4.6  
pgaudit | 1.1.3 | 1.2.3 | 1.3.2 | 1.4.1 | no change  
pglogical | 2.3.3 | 2.3.3 | 2.3.3 | 2.3.3 | 2.3.3  
pl/proxy | 2.10.0 | 2.10.0 | 2.10.0 | 2.10.0 | 2.10.0  
postgis | 2.3.11 | 2.4.9 | 2.5.5 | 3.0.2 | 3.0.2  
  
## May 19, 2021

Feature

Cloud SQL supports the preview version of the [out-of-disk recommender](https://docs.cloud.google.com/sql/docs/mysql/using-ood-recommender). This feature proactively generates recommendations that help you reduce the risk of downtime that might be caused by your instances running out of disk space. These recommendations can be applied when a Cloud SQL instance is trending towards the storage limit.

## April 23, 2021

Feature

The following PostgreSQL minor versions are now available. If you use maintenance windows, you might not yet have the minor version. In this case, you will see the new minor version once your maintenance update occurs. To find your maintenance window or manage maintenance updates, see [Finding and setting maintenance windows](https://docs.cloud.google.com/sql/docs/postgres/set-maintenance-window).

  * 9.6.20 is upgraded to 9.6.21.
  * 10.15 is upgraded to 10.16.
  * 11.10 is upgraded to 11.11.
  * 12.5 is upgraded to 12.6.
  * 13.1 is upgraded to 13.2.



For more information about the content of these minor versions, please see [the PostgreSQL release notes](https://www.postgresql.org/about/news/postgresql-132-126-1111-1016-9621-and-9525-released-2165/).

## April 06, 2021

Feature

Cloud SQL for PostgreSQL now lets you use IAM database authentication with the Cloud SQL Auth proxy. The Cloud SQL Auth proxy is able to request and refresh OAuth 2.0 access tokens, ensuring that long-lived processes or applications that rely on connection pooling can have stable connections. To learn more, see [Using IAM database authentication with the Cloud SQL Auth proxy](https://docs.cloud.google.com/sql/docs/postgres/iam-logins#using_with_the).

## March 31, 2021

Feature

Cloud SQL for PostgreSQL flags are now generally available. See [supported PostgreSQL flags](https://docs.cloud.google.com/sql/docs/postgres/flags#list-flags-postgres) for more information.

## March 24, 2021

Feature

Support for [europe-central2 (Warsaw )](https://docs.cloud.google.com/sql/docs/postgres/locations#location-r).

## March 19, 2021

Feature

The following extensions in Cloud SQL for PostgreSQL are [generally available](https://docs.cloud.google.com/sql/docs/postgres/extensions#miscellaneous-extensions): 

  * **pg_partman.** Enables you to create and manage time-based and serial-based table partition sets.
  * **pgTAP.** Provides a unit testing framework for PostgreSQL, written in PL/pgSQL and PL/SQL.



## February 24, 2021

Change

Cloud SQL now offers faster maintenance, with average connectivity loss lasting 90 seconds or less on average. See more about [maintenance timelines](https://docs.cloud.google.com/sql/docs/postgres/maintenance#how_long_does_maintenance_take).

## February 22, 2021

Feature

The following PostgreSQL minor versions are now available. If you use maintenance windows, you might not yet have the minor version. In this case, you will see the new minor version once your maintenance update occurs. To find your maintenance window or manage maintenance updates, see [Finding and setting maintenance windows](https://docs.cloud.google.com/sql/docs/postgres/set-maintenance-window).

  * PostgreSQL 9.6.19 is upgraded to 9.6.20.
  * PostgreSQL 10.14 is upgraded to 10.15.
  * PostgreSQL 11.9 is upgraded to 11.10.
  * PostgreSQL 12.4 is upgraded to 12.5.
  * PostgreSQL 13 is upgraded to 13.1.



## February 10, 2021

Feature

The Cloud SQL Admin API v1beta4 is now generally available. The URL for the Admin API will continue to refer to v1beta4 for backward compatibility. To start using the Cloud SQL Admin API now, see [Using the Cloud SQL Admin API](https://docs.cloud.google.com/sql/docs/postgres/admin-api).

## January 28, 2021

Feature

Query Insights is now generally available. Query Insights helps you detect, diagnose, and prevent query performance problems for Cloud SQL databases. It provides self-service, intuitive monitoring, and diagnostic information that goes beyond detection to help you to identify the root cause of performance problems.

To learn more, see [Improving query performance](https://docs.cloud.google.com/sql/docs/postgres/using-query-insights).

## January 19, 2021

Feature

Database auditing in Cloud SQL for PostgreSQL is [generally available](https://docs.cloud.google.com/sql/docs/postgres/pg-audit), through the open-source pgAudit extension. Using this extension, you can selectively record and track SQL operations performed against a given database instance.

The pgAudit extension helps you configure many of the logs often required to comply with government, financial, and ISO certifications.

## January 13, 2021

Feature

Cloud SQL now exposes the metric `database/memory/total_usage`. This metric provides visibility into the database working set (including buffer cache). You can find this metric in the [Metrics explorer](https://docs.cloud.google.com/monitoring/charts/metrics-explorer) within the Monitoring dashboard. 

For more information about `database/memory/total_usage`, see [Cloud SQL Metrics](https://docs.cloud.google.com/monitoring/api/metrics_gcp#gcp-cloudsql).

## December 21, 2020

Feature

IAM database authentication for Cloud SQL for PostgreSQL is now generally available. To get started using IAM database authentication, see the [Overview of Cloud SQL IAM database authentication](https://docs.cloud.google.com/sql/docs/postgres/authentication).

## December 17, 2020

Feature

Cloud SQL has expanded support for PostgreSQL extensions. Three additional PostgreSQL extensions are now available: 

  * dblink
  * ip4r
  * prefix



For additional information, see [PostgreSQL extensions](https://docs.cloud.google.com/sql/docs/postgres/extensions).

Feature

The following PostgreSQL minor versions have been upgraded:

  * PostgreSQL 9.6.18 is upgraded to 9.6.19.
  * PostgreSQL 10.13 is upgraded to 10.14.
  * PostgreSQL 11.8 is upgraded to 11.9.
  * PostgreSQL 12.3 is upgraded to 12.4.



## December 16, 2020

Feature

Cloud SQL for PostgreSQL now supports the effective_cache_size flag.

## November 19, 2020

Feature

Cloud SQL for PostgreSQL now supports [retention settings for point-in-time recovery](https://docs.cloud.google.com/sql/docs/postgres/backup-recovery/backups#retention). You have the option of retaining logs, used for point-in-time recovery, for shorter periods (1 to 7 days). The default setting is 7.

Feature

Cloud SQL for PostgreSQL now supports [retention settings for automated backups](https://docs.cloud.google.com/sql/docs/postgres/backup-recovery/backups#retention). You can configure retention of your automated backups for shorter or longer periods (1 to 365 days). The default setting remains 7 days.

## November 05, 2020

Feature

PostgreSQL version 13 is now generally available. To start using PostgreSQL 13, see [Creating instances](https://docs.cloud.google.com/sql/docs/postgres/create-instance).

## October 12, 2020

Feature

Cloud SQL for PostgreSQL now offers IAM database authentication to help you better monitor and manage access for users and service accounts to databases. This feature allows users and service accounts to use IAM credentials to log into PostgreSQL instances. To learn more about how IAM database authentication works, see the [Overview of Cloud SQL IAM database authentication](https://docs.cloud.google.com/sql/docs/postgres/authentication). To configure an instance, see [Configuring instances for IAM database authentication](https://docs.cloud.google.com/sql/docs/postgres/create-edit-iam-instances). To create users or service accounts, see [Creating and managing users that use IAM database authentication](http://cloud.google.com/sql/docs/postgres/create-manage-iam-users).

Feature

Cloud SQL now offers "deny maintenance periods". With [deny maintenance periods](https://docs.cloud.google.com/sql/docs/postgres/maintenance#deny), you can prevent automatic maintenance from occurring during a specific time period. For example, the end-of-year holiday season is a time of peak load that requires heightened focus on infrastructure stability for many retail businesses. By setting a deny maintenance period from mid-October to mid-January, these businesses can prevent planned upgrades from Cloud SQL during their busiest time of year.

Feature

Database auditing in Cloud SQL for PostgreSQL is [available](https://docs.cloud.google.com/sql/docs/postgres/pg-audit) through the open-source pgAudit extension. Using this extension, you can selectively record and track SQL operations performed against a given database instance.

The pgAudit extension helps you configure many of the logs often required to comply with government, financial, and ISO certifications.

## September 15, 2020

Feature

Cloud SQL now offers serverless export. With [serverless export](https://docs.cloud.google.com/sql/docs/postgres/import-export/exporting#standard-offload), Cloud SQL performs the export from a temporary instance. Offloading the export operation allows databases on the primary instance to continue to serve queries and perform other operations at the usual performance rate.

Feature

The following PostgreSQL minor versions have been upgraded:

  * PostgreSQL 9.6.16 is upgraded to 9.6.18.
  * PostgreSQL 10.11 is upgraded to 10.13.
  * PostgreSQL 11.6 is upgraded to 11.8.
  * PostgreSQL 12.1 is upgraded to 12.3.



## July 09, 2020

Feature

Cloud SQL now supports [point-in-time recovery (PITR) for PostgreSQL](https://docs.cloud.google.com/sql/docs/postgres/backup-recovery/pitr). Point-in-time recovery helps you recover an instance to a specific point in time. For example, if an error causes a loss of data, you can recover a database to its state before the error occurred.

## June 23, 2020

Feature

Committed use discounts (CUDs) are now available to purchase for Cloud SQL. CUDs provide discounted prices in exchange for your commitment to use a minimum level of resources for a specified term. With committed use discounts for Cloud SQL, you can earn a deep discount off your cost of use in exchange for committing to continuously use database instances in a particular region for a 1- or 3-year term. See the [documentation](https://docs.cloud.google.com/sql/docs/mysql/cud) for more details.

## June 08, 2020

Feature

Support for [asia-southeast2](https://docs.cloud.google.com/sql/docs/mysql/locations) region (Jakarta).

## May 21, 2020

Feature

PostgreSQL version 12 is now generally available. To start using PostgreSQL 12, see [Creating instances](https://docs.cloud.google.com/sql/docs/postgres/create-instance).

## May 15, 2020

Feature

PostgreSQL 9.6 minor version is upgraded to 9.6.16. PostgreSQL 10 minor version is upgraded to 10.11. PostgreSQL 11 minor version is upgraded to 11.6. PostgreSQL 12 minor version is upgraded to 12.1.

## May 11, 2020

Feature

Cloud SQL has expanded support for PostgreSQL extensions. Eight additional PostgreSQL extensions are now available: 

  * pageinspect
  * pgfincore
  * pg_freespacemap
  * pg_repack
  * pg_visibility
  * PL/Proxy
  * postgres_fdw
  * postgresql-hll



For information about these newly-added extensions, see [PostgreSQL extensions](https://docs.cloud.google.com/sql/docs/postgres/extensions).

## April 20, 2020

Feature

Support for [us-west4](https://docs.cloud.google.com/sql/docs/postgres/locations) region (Las Vegas).

## March 27, 2020

Feature

PostgreSQL version 12 is now Beta. To start using PostgreSQL 12, see [Creating instances](https://docs.cloud.google.com/sql/docs/postgres/create-instance).

Feature

PostgreSQL version 10 is now generally available. To start using PostgreSQL 10, see [Creating instances](https://docs.cloud.google.com/sql/docs/postgres/create-instance).

## March 24, 2020

Feature

Cloud SQL now supports 96-core machine types for MySQL, Postgres, and SQL Server instances. For pricing-related information, see the [Pricing page](https://cloud.google.com/sql/pricing).

## March 16, 2020

Feature

Cloud SQL now supports read replicas in a different region than that of the primary instance, providing additional protection against regional outages and improving read performance by making replicas available closer to your application. To get started, see [Cross-region replicas](https://docs.cloud.google.com/sql/docs/postgres/replication/cross-region-replicas). 

Cloud SQL instances using [private IP](https://docs.cloud.google.com/sql/docs/postgres/private-ip) are now accessible across regions, at the regular cross-region network egress cost.

## February 24, 2020

Feature

Support for us-west3 region (Salt Lake City).

## January 30, 2020

Feature

PostgreSQL version 10 is now Beta. To start using PostgreSQL 10, see [Creating Instances](https://docs.cloud.google.com/sql/docs/postgres/create-instance).

## January 24, 2020

Feature

Support for [asia-northeast3](https://docs.cloud.google.com/sql/docs/postgres/locations) region (Seoul).

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

Cloud SQL now supports customer-managed encryption keys (CMEK). With CMEK, you can encrypt Cloud SQL instances using a key you manage. To learn more about CMEK, see the [Overview of customer managed encryption keys (CMEK)](https://docs.cloud.google.com/sql/docs/postgres/cmek). To start using CMEK, see [Using customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/sql/docs/postgres/configure-cmek).

## September 27, 2019

Feature

PostgreSQL version 11 is now generally available. PostgreSQL 11 is the default version when creating new instances. To start using PostgreSQL 11, see [Creating Instances](https://docs.cloud.google.com/sql/docs/postgres/create-instance).

## June 25, 2019

Feature

This release increases the maximum data storage for instances of MySQL (MySQL Second Generation) and PostgreSQL. The maximum data storage is increased from 10,230 GB to 30,720 GB. For Cloud SQL storage limits, see [Limits](https://docs.cloud.google.com/sql/docs/postgres/quotas#limits). You can limit your automatic storage increases; see [Automatic storage increase limit](https://docs.cloud.google.com/sql/docs/postgres/instance-settings#automatic-storage-increase-limit-2ndgen).

## May 24, 2019

Feature

Cloud SQL now allows you to specify a location for backups, and to restrict data to a single region. To learn about custom backup locations, see [Custom backup locations](https://docs.cloud.google.com/sql/docs/postgres/backup-recovery/backups#custom-backup-location). To learn how to set a custom location for a backup, see [Setting and viewing a custom location for backups](https://docs.cloud.google.com/sql/docs/postgres/backup-recovery/backing-up#locationbackups).

## April 18, 2019

Feature

Support for [asia-northeast2](https://docs.cloud.google.com/sql/docs/postgres/locations) region (Osaka, Japan).

## April 09, 2019

Feature

Cloud SQL now supports PostgreSQL version 11.1 Beta. To start using PostgreSQL 11 Beta, see [Creating Instances](https://docs.cloud.google.com/sql/docs/postgres/create-instance).

## April 03, 2019

Feature

Support added for 122 MySQL flags and 96 PostgreSQL flags. See [Supported PostgreSQL Flags](https://docs.cloud.google.com/sql/docs/postgres/flags#list-flags-postgres) and [Supported MySQL Flags](https://docs.cloud.google.com/sql/docs/mysql/flags#list-flags-mysql).

## March 11, 2019

Feature

Support for [europe-west6](https://docs.cloud.google.com/sql/docs/postgres/locations) region (Zürich, Switzerland).

## February 13, 2019

Change

Cloud SQL for PostgreSQL connection limits are now double when memory is 6 GiB or higher. See [the connection limits table](https://docs.cloud.google.com/sql/docs/quotas#fixed-limits) for details.

## December 06, 2018

Feature

GA support for [Private IP connectivity](https://docs.cloud.google.com/sql/docs/postgres/private-ip).

## November 06, 2018

Feature

Support for CSV format for PostgreSQL instance [imports](https://docs.cloud.google.com/sql/docs/postgres/import-export/importing#csv) and [exports](https://docs.cloud.google.com/sql/docs/postgres/import-export/exporting#csv).

## October 01, 2018

Feature

Support for [asia-east2 region](https://docs.cloud.google.com/sql/docs/postgres/locations) (Hong Kong).

## September 01, 2018

Feature

Beta support for [private IP](https://docs.cloud.google.com/sql/docs/postgres/private-ip) (private services access) connectivity.

Change

[Proxy version 1.12](https://github.com/GoogleCloudPlatform/cloudsql-proxy/releases/tag/1.12) released.

## August 01, 2018

Change

[PostGIS extension](https://docs.cloud.google.com/sql/docs/postgres/extensions#postgis) includes full support for JSON-C.

## July 01, 2018

Feature

Support for [us-west2 region](https://docs.cloud.google.com/sql/docs/postgres/instance-locations) (Los Angeles).

## June 01, 2018

Feature

Support for connecting from [Cloud Functions](https://docs.cloud.google.com/sql/docs/postgres/connect-functions) Beta.

Feature

Support for [rotating SSL certificates](https://docs.cloud.google.com/sql/docs/postgres/configure-ssl-instance#how-rotation-works).

Feature

Support for [europe-north1 region](https://docs.cloud.google.com/sql/docs/postgres/instance-locations) (Finland).

## May 01, 2018

Feature

Support for [asia-southeast1 region](https://docs.cloud.google.com/sql/docs/postgres/instance-locations) (Singapore).

## April 01, 2018

Feature

GA support for [Cloud SQL for PostgreSQL](https://docs.cloud.google.com/sql/docs/postgres).

## March 01, 2018

Feature

Support for [europe-west4 region](https://docs.cloud.google.com/sql/docs/postgres/instance-locations) (Netherlands).

## February 01, 2018

Change

[Maximum concurrent connections to App Engine](https://docs.cloud.google.com/sql/docs/mysql/faq#sizeqps) updated from 12 to 60.

## January 01, 2018

Change

Connection limits for PostgreSQL instances changed. [Learn more](https://docs.cloud.google.com/sql/docs/postgres/faq#sizeqps).

Feature

Support for [northamerica-northeast1 region](https://docs.cloud.google.com/sql/docs/postgres/instance-locations) (Montréal).

Change

MySQL 5.6 minor version upgraded to 5.6.36.

## November 01, 2017

Feature

Beta support for [the high availability configuration](https://docs.cloud.google.com/sql/docs/postgres/high-availability) and [replication](https://docs.cloud.google.com/sql/docs/postgres/replication/create-replica) for PostgreSQL instances.

## October 01, 2017

Feature

Support for [asia-south1 region](https://docs.cloud.google.com/sql/docs/postgres/instance-locations) (Mumbai).

Change

[Proxy version 1.11](https://github.com/GoogleCloudPlatform/cloudsql-proxy/releases/tag/1.11) released.

## September 01, 2017

Feature

Support for 64-core [machine types](https://docs.cloud.google.com/sql/docs/mysql/instance-settings#machine-type-2ndgen) for MySQL instances and 64 cores for PostgreSQL instances.

Feature

Support for [southamerica-east1 region](https://docs.cloud.google.com/sql/docs/postgres/instance-locations) (São Paulo).

## August 01, 2017

Feature

Support for [europe-west3 region](https://docs.cloud.google.com/sql/docs/postgres/instance-locations) (Frankfurt).

## June 01, 2017

Feature

Support for the [JDBC Socket Library for PostgreSQL](https://docs.cloud.google.com/sql/docs/postgres/connect-external-app#java).

Feature

Support for the following PostgreSQL [extensions](https://docs.cloud.google.com/sql/docs/postgres/extensions): `btree-gin`, `btree-gist`, `chkpass`, `citext`, `cube`, `dict_int`, `dict_xsyn`, `earthdistance`, `intagg`, `intarray`, `isn`, `ltree`, `pgstattuple`, `pg_trgm`, `tablefunc`, `tsm_system_rows`, `tsm_system_time`, `unaccent`, `uuid-ossp`.

Feature

Support for [australia-southeast1 region](https://docs.cloud.google.com/sql/docs/postgres/instance-locations) (Sydney).

Feature

Support for [labels](https://docs.cloud.google.com/sql/docs/postgres/label-instance).

Change

[Proxy version 1.10](https://github.com/GoogleCloudPlatform/cloudsql-proxy/releases) released.

Feature

Support for [europe-west2 region](https://docs.cloud.google.com/sql/docs/postgres/instance-locations) (London).

## May 01, 2017

Feature

GA support for Second Generation and PostgreSQL instances in version 157.0.0 of the `gcloud` command-line tool. The `beta` version is no longer required for these instances.

Feature

Support for [us-west1 region](https://docs.cloud.google.com/sql/docs/postgres/instance-locations) (Oregon).

Feature

Support for [us-east4 region](https://docs.cloud.google.com/sql/docs/postgres/instance-locations) (Northern Virginia).

## April 01, 2017

Change

[Proxy version 1.09](https://github.com/GoogleCloudPlatform/cloudsql-proxy/releases) released.

## March 01, 2017

Feature

[Cloud SQL for PostgreSQL](https://docs.cloud.google.com/sql/docs/postgres/features#postgres) Beta availability.

To provide feedback on the beta release, go to [our Cloud SQL user forum](https://googlecloudplatform.uservoice.com/forums/302613-cloud-sql).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
