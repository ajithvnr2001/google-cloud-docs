---
url: https://docs.cloud.google.com/sql/docs/sqlserver/release-notes/
title: Cloud SQL for SQL Server release notes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:51:08.634727+00:00
---

# Cloud SQL for SQL Server release notes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/sqlserver/release-notes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ SQL Server ](https://docs.cloud.google.com/sql/docs/sqlserver)
  * [ Resources ](https://docs.cloud.google.com/sql/docs/sqlserver/resources)



Send feedback 

#  Cloud SQL for SQL Server release notes Stay organized with collections  Save and categorize content based on your preferences. 

This page documents production updates to Cloud SQL for SQL Server. You can check this page for announcements about new or updated features, bug fixes, known issues, and deprecated functionality. 

You can see the latest product updates for all of Google Cloud on the [ Google Cloud](https://docs.cloud.google.com/release-notes) page, browse and filter all release notes in the [Google Cloud console](https://console.cloud.google.com/release-notes), or programmatically access release notes in [BigQuery](https://console.cloud.google.com/bigquery?p=bigquery-public-data&d=google_cloud_release_notes&t=release_notes&page=table). 

To get the latest product updates delivered to you, add the URL of this page to your [feed reader](https://wikipedia.org/wiki/Comparison_of_feed_aggregators), or add the [feed URL](https://docs.cloud.google.com/feeds/cloud-sql-server-release-notes.xml) directly. 

## October 13, 2026

Feature

[Private Service Connect](https://docs.cloud.google.com/sql/docs/sqlserver/about-private-service-connect) is now the default private IP connectivity option when you create a Cloud SQL for SQL Server instance in a new Google Cloud project. Private Service Connect lets you connect to your instance from multiple Virtual Private Cloud (VPC) networks across different groups, projects, or organizations, and supports automatic endpoint and DNS record provisioning. When you configure private IP for an instance, you can still choose to use private services access or both connectivity options.

For more information, see [Private IP configuration options](https://docs.cloud.google.com/sql/docs/sqlserver/private-ip) and [Configure Private Service Connect](https://docs.cloud.google.com/sql/docs/sqlserver/configure-private-service-connect).

## September 28, 2026

Breaking

To improve security, removed the `cloudsql.instances.export` permission from the following roles:

  * Cloud SQL Viewer (`roles/cloudsql.viewer`)
  * Basic Reader (`roles/reader`)
  * Basic Viewer (Legacy) (`roles/viewer`)



To retain export capabilities, assign the Cloud SQL Editor (`roles/cloudsql.editor`) role or update custom roles to include the `cloudsql.instances.export` permission.

For more information, see [Cloud SQL roles](https://docs.cloud.google.com/sql/docs/sqlserver/iam-roles).

## September 21, 2026

Feature

The [C4 machine series](https://docs.cloud.google.com/sql/docs/sqlserver/machine-series-overview#c4) is available for Cloud SQL for SQL Server Enterprise Plus instances in the following regions:

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



## September 14, 2026

Deprecated

Beginning April 12, 2027, you won't be able to create new instances of Cloud SQL for SQL Server 2017. Starting on October 13, 2027, SQL Server 2017 will reach end of life (EOL) and Microsoft will stop releasing [security updates](https://learn.microsoft.com/en-us/sql/sql-server/end-of-support/sql-server-end-of-support-overview?view=sql-server-ver17#understand-the-sql-server-lifecycle). Cloud SQL for SQL Server will stop supporting SQL Server 2017 after this date.

For more information, see [Database versions and version policies](https://docs.cloud.google.com/sql/docs/sqlserver/db-versions).

## September 08, 2026

Feature

[Regional endpoints (REP)](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rep) are now generally available ([GA](https://cloud.google.com/products#product-launch-stages)) for the Cloud SQL for SQL Server Admin API.

Regional endpoints let you interact with Cloud SQL for SQL Server instances using regionalized URLs (such as `sqladmin.[{region}](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rep#supported_regions).rep.googleapis.com`) rather than through a single global endpoint.

Regional endpoints provide regional frontend and load balancing infrastructure that improves data residency by keeping network traffic within the same region as the instance. This reduces the instance's dependency on global frontend infrastructure.

Regional endpoints have strong regional isolation, so the failure of a load balancer or frontend in one region doesn't affect any other region. Regional service load balancers have a separate, regionally isolated control plane.

Regional endpoints are designed to meet stringent data residency and sovereignty standards, such as ITAR and Assured Workloads Regions, ensuring data in transit remains within the committed region.

Certificate management and TLS termination occurs within each region, on the regional load balancer, so data remains encrypted until it reaches its destination region and stays within that region while being processed there.

## September 04, 2026

Feature

Cloud SQL for SQL Server supports the `sp_help_revlogin` stored procedure in the `msdb` database. You can enable this stored procedure by configuring the `cloud sql enable sp_help_revlogin` database flag to export SQL Server logins, password hashes, and security identifiers (SIDs) when migrating databases or synchronizing logins.

For more information, see [Export SQL Server logins](https://docs.cloud.google.com/sql/docs/sqlserver/export-logins) and [Configure database flags](https://docs.cloud.google.com/sql/docs/sqlserver/flags).

Feature

Cloud SQL for SQL Server now supports connecting to instances with write endpoints using the Cloud SQL Auth Proxy or Cloud SQL language connectors. When you configure the proxy or a language connector with a write endpoint DNS name, connections are redirected automatically to the new primary instance during replica failover or switchover.

For more information, see [Connect to an instance using a write endpoint](https://docs.cloud.google.com/sql/docs/sqlserver/connect-to-instance-using-write-endpoint).

Feature

The [C4 machine series](https://docs.cloud.google.com/sql/docs/sqlserver/machine-series-overview#c4) is now available for Cloud SQL for SQL Server Enterprise Plus instances in the following regions:

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

For more information about in-place upgrades and downgrades, see [Upgrade in place](https://docs.cloud.google.com/sql/docs/sqlserver/upgrade-in-place).

## August 27, 2026

Feature

Cloud SQL now makes it easier to configure [Private Service Connect](https://docs.cloud.google.com/sql/docs/sqlserver/about-private-service-connect) for your Cloud SQL instance. When you create an instance that's enabled with Private Service Connect, you can choose to automatically create the service connection policy and endpoint in the VPC network that you want to use with Private Service Connect.

For more information, see [Configure Private Service Connect](https://docs.cloud.google.com/sql/docs/sqlserver/configure-private-service-connect).

## August 11, 2026

Feature

You can now use the `update_user` tool in the Cloud SQL remote MCP server to update passwords for Cloud SQL for SQL Server database users.

For more information, see [Available tools](https://docs.cloud.google.com/sql/docs/sqlserver/use-cloudsql-mcp#available-tools).

Feature

The Cloud SQL remote MCP server now supports specialized endpoint URLs (toolsets) for `/readonly` and `/instance_manage`. Specialized toolset URLs let you restrict the set of exposed MCP tools based on your security and workflow requirements.

For more information, see [Available toolsets](https://docs.cloud.google.com/sql/docs/sqlserver/use-cloudsql-mcp#available-toolsets).

## August 07, 2026

Change

Newly created instances configured with [high availability (HA)](https://docs.cloud.google.com/sql/docs/sqlserver/high-availability) now have [Knowledge Catalog (formerly Dataplex Universal Catalog)](https://docs.cloud.google.com/sql/docs/sqlserver/dataplex-catalog-integration) enabled by default.

Cloud SQL for SQL Server instances send updates and metadata to Knowledge Catalog to help support data discovery.

You can either verify enablement or [disable the feature](https://docs.cloud.google.com/sql/docs/sqlserver/dataplex-catalog-integration#deactivate-dataplex-catalog) using the Google Cloud console.

For more information, see [Manage your Cloud SQL resources using Knowledge Catalog](https://docs.cloud.google.com/sql/docs/sqlserver/dataplex-catalog-integration).

## August 04, 2026

Feature

[DNS automation](https://docs.cloud.google.com/sql/docs/sqlserver/configure-dns#dns-auto) is now generally available ([GA](https://cloud.google.com/products#product-launch-stages)) on Cloud SQL instances where Private Service Connect is enabled.

You can use DNS automation to provision and manage per-instance DNS records automatically. On Enterprise Plus edition instances where DNS automation is enabled, you can also enable a global write endpoint DNS that automatically resolves to your current primary instance.

## August 03, 2026

Change

You can change the backup plan for your [Cloud SQL enhanced backups](https://docs.cloud.google.com/sql/docs/sqlserver/backup-recovery/manage-enhanced-backups) without first removing the existing plan. For more information, see [Change your instance's associated backup plan](https://docs.cloud.google.com/sql/docs/sqlserver/backup-recovery/manage-enhanced-backups#change-plan).

## July 31, 2026

Change

Starting on August 1, 2026, when you create or clone a Cloud SQL instance enabled with Private Service Connect, or when you enable Private Service Connect for an existing instance, then [connection reconciliation](https://docs.cloud.google.com/vpc/docs/about-controlling-access-published-services#connection-reconciliation) behavior is enabled by default and can't be disabled.

When you remove a project from the list of allowed projects, all existing Private Service Connect connections from the removed project are immediately closed (reconciled). This means that applications using Private Service Connect endpoints in those removed projects can't continue to connect to the Cloud SQL instance using those endpoints.

For more information, see [Allowed Private Service Connect projects](https://docs.cloud.google.com/sql/docs/sqlserver/about-private-service-connect#allowed-psc-projects).

Feature

Cloud SQL for SQL Server now supports executing SQL statements using the [Cloud SQL Data API](https://docs.cloud.google.com/sql/docs/sqlserver/executesql-instance).

## July 29, 2026

Feature

Cloud SQL for SQL Server now supports significantly faster re-encryption of instances and replicas protected by customer-managed encryption keys (CMEKs), and re-encryption now completes with zero downtime. The steps to re-encrypt your instances and replicas are unchanged, but the operation now re-encrypts the underlying disks in-place, without creating re-encryption backups.

For more information, see [Re-encrypt an existing CMEK-enabled instance or replica](https://docs.cloud.google.com/sql/docs/sqlserver/configure-cmek#reencrypt).

## June 24, 2026

Change

Cloud SQL now supports Private Service Connect outbound connectivity on the following additional types of instances:

  * Read replica instances.

  * Instances that use advanced disaster recovery features such as switchover and failover operations.

  * Primary instances that have replicas.




For more information about Private Service Connect outbound connectivity see [About Private Service Connect](https://docs.cloud.google.com/sql/docs/sqlserver/about-private-service-connect#psc-outbound).

## June 22, 2026

Feature

Customer-managed encryption key (CMEK) support for Cloud SQL enhanced backups is generally available. You can protect your CMEK-enabled Cloud SQL instances using Google Cloud Backup and DR Service.

For more information, see [Choose your backup option](https://docs.cloud.google.com/sql/docs/sqlserver/backup-recovery/backup-options).

## May 12, 2026

Change

The command for upgrading Cloud SQL instances to the new network architecture has been re-enabled.

For more information, see [Upgrade an instance to the new network architecture](https://docs.cloud.google.com/sql/docs/sqlserver/upgrade-cloud-sql-instance-new-network-architecture) .

## May 11, 2026

Feature

Cloud SQL for SQL Server now supports regional endpoints for the Cloud SQL Admin API. This feature lets you direct your API calls to a region-specific endpoint. Using a regional endpoint enhances data locality and helps meet strict compliance expectations.

This feature includes: * **Regional boundary restrictions** : Cloud SQL regional endpoints enforce strict matching. The region of the target API resource must match the region of the endpoint exactly. Otherwise, the request is rejected with a 4xx error. * **Restricted API visibility** : When you use a regional endpoint, the Instance.List API only returns resources located within that specific region.

For more information, see [Cloud SQL regional endpoints](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rep).

This feature is in [Preview](https://cloud.google.com/products#product-launch-stages).

## May 04, 2026

Feature

Cloud SQL for SQL Server now supports PolyBase ([GA](https://cloud.google.com/products#product-launch-stages)).

With PolyBase, your Cloud SQL for SQL Server instance uses Transact-SQL (T-SQL) commands to directly query data stored in external data sources as if the data is stored in local tables. You don't need to install separate client connection software.

For more information, see [About PolyBase](https://docs.cloud.google.com/sql/docs/sqlserver/about-polybase).

## April 30, 2026

Feature

If a specific active query is blocked or running much longer than expected, it can block other dependent queries. Cloud SQL for SQL Server offers an optional feature that lets you view and terminate blocking queries.

For more information, see [Blocked active queries](https://docs.cloud.google.com/sql/docs/sqlserver/monitor-active-queries#blocked-active-queries) ([Preview](https://cloud.google.com/products#product-launch-stages)).

## April 20, 2026

Feature

You can use the [Database Insights remote MCP server](https://docs.cloud.google.com/sql/docs/sqlserver/reference/mcp/databaseinsights/mcp) to analyze Cloud SQL for SQL Server's performance and system metrics. This feature is in [GA](https://cloud.google.com/products#product-launch-stages).

## April 18, 2026

Feature

Newly created Cloud SQL instances are integrating with Knowledge Catalog (formerly Dataplex Universal Catalog) for data discovery. As part of this automatic enablement, we will send metadata to Knowledge Catalog. You can verify if your instance is enabled for integration with Knowledge Catalog by looking at the configuration pane in the Knowledge Catalog console. If you don't want your instance to be integrated with Knowledge Catalog, you can [turn off this feature](https://docs.cloud.google.com/sql/docs/sqlserver/dataplex-catalog-integration#deactivate-dataplex-catalog).

For more information, see [Create a new instance with Knowledge Catalog integration enabled](https://docs.cloud.google.com/sql/docs/sqlserver/dataplex-catalog-integration#enable-new).

## April 17, 2026

Feature

You can now integrate Cloud SQL for SQL Server with Vertex AI and third-party models ([Preview](https://cloud.google.com/products#product-launch-stages)).

By integrating your Cloud SQL for SQL Server instance with Vertex AI, you can generate vector embeddings from models hosted in Vertex AI directly from your Cloud SQL instance.

Cloud SQL for SQL Server supports model endpoints from the following sources:

  * Vertex AI
  * Hugging Face
  * OpenAI



For more information, see [Integrate Cloud SQL for SQL Server with Vertex AI](https://docs.cloud.google.com/sql/docs/sqlserver/integrate-cloud-sql-with-vertex-ai).

## April 16, 2026

Feature

You can use [DNS automation](https://docs.cloud.google.com/sql/docs/sqlserver/about-private-service-connect#dns-automation) on Cloud SQL instances where Private Service Connect is enabled to provision and manage per-instance DNS records automatically. On Enterprise Plus edition instances where DNS automation is enabled, you can also enable a global write endpoint DNS that automatically resolves to your current primary instance.

This feature is in [Preview](https://cloud.google.com/products#product-launch-stages).

Feature

The [Cloud SQL remote MCP server](https://docs.cloud.google.com/sql/docs/sqlserver/use-cloudsql-mcp) is generally available ([GA](https://cloud.google.com/products#product-launch-stages)). The Cloud SQL remote MCP server lets you interact easily with Cloud SQL instances from LLMs, AI applications, and AI-enabled development platforms.

## April 14, 2026

Breaking

As of April 10, 2026, you can create, run, and edit [Gemini Cloud Assist investigations](https://docs.cloud.google.com/cloud-assist/investigations) only if you have a [Premium Support contract](https://cloud.google.com/support/premium). You can use Gemini Cloud Assist investigations to [monitor and troubleshoot your Cloud SQL instance with AI assistance](https://docs.cloud.google.com/sql/docs/sqlserver/monitor-troubleshoot-with-ai).

If you ran an investigation prior to April 10, 2026, then the results of the investigation continue to be available to you in the Google Cloud console.

## April 06, 2026

Feature

Cloud SQL for SQL Server now supports SQL Server 2025 ([GA](https://cloud.google.com/products#product-launch-stages)):

  * SQL Server 2025 Standard
  * SQL Server 2025 Enterprise
  * SQL Server 2025 Express



For more information, see [Database versions and version policies](https://docs.cloud.google.com/sql/docs/sqlserver/db-versions) and [Choose a machine series](https://docs.cloud.google.com/sql/docs/sqlserver/machine-series-overview).

Feature

[Cloud SQL for SQL Server integration with Microsoft Entra ID](https://docs.cloud.google.com/sql/docs/sqlserver/integration-with-microsoft-entra-id) ([GA](https://cloud.google.com/products#product-launch-stages)) provides centralized identity and access management (IAM) for your databases using your existing Microsoft Entra ID tenant.

Feature

If the storage capacity of a Cloud SQL instance is larger than your application needs, then you can manually reduce, or shrink, your storage capacity to a smaller size.

Depending on underlying disk size, storage shrink operations might incur considerable downtime. If your instance requires limited downtime, rather than using storage shrink capabilities, we recommend migrating your data to a new, smaller instance using Database Migration Service.

For more information, see [About storage shrink](https://docs.cloud.google.com/sql/docs/sqlserver/about-storage-shrink).

## April 02, 2026

Feature

Cloud SQL for SQL server read pools are now generally available and provide operational simplicity and scaling for your read workloads.

Read pools provide a single endpoint in front of up to seven read pool nodes and automatically load balance traffic.

You can scale your read pool in several ways:

  * **Scale in or out** : scale load balancing capacity horizontally by modifying the number of read pool nodes in the read pool. Each read pool supports between 1 and 7 read pool nodes.

  * **Scale up or down** : scale load balancing capacity vertically by modifying the machine type associated with a read pool node. Once defined, configuration is uniformly applied across each read pool node in the read pool.




For more information, see [About read pools](https://docs.cloud.google.com/sql/docs/sqlserver/about-read-pools) .

## March 17, 2026

Change

Point-in-time recovery (PITR) default enablement behavior has changed:

  * PITR is now enabled by default when you create a [Cloud SQL Enterprise edition](https://docs.cloud.google.com/sql/docs/sqlserver/editions-intro) instance in the Google Cloud console.
  * PITR is enabled by default when you create a [Cloud SQL Enterprise Plus edition](https://docs.cloud.google.com/sql/docs/sqlserver/editions-intro) instance, regardless of the method used.



For more information, see [Configure point-in-time recovery (PITR)](https://docs.cloud.google.com/sql/docs/sqlserver/backup-recovery/configure-pitr) .

Feature

Cloud SQL supports cross-project PITR operations for instances protected by backup and DR ([GA](https://cloud.google.com/products#product-launch-stages)).

This feature lets you restore a Cloud SQL instance to a project other than the project where either the source instance or the backup vault is located.

For more information, see [Perform a cross-project PITR](https://docs.cloud.google.com/sql/docs/sqlserver/backup-recovery/pitr#perform_a_cross-project_pitr) .

Feature

[Multi-region backup vaults for Cloud SQL enhanced backups](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-vault#multi-regions) are generally available (GA).

This feature lets you store your backup data in multi-region storage locations, providing higher availability and protection against regional outages.

For more information, see [Enhanced backups](https://docs.cloud.google.com/sql/docs/sqlserver/backup-recovery/backup-options#enhanced-backups) .

## March 13, 2026

Feature

You can now enable automatic server certificate rotation for your Cloud SQL instance. This feature is specifically designed for instances utilizing the Certificate Authority Service (CAS). Automatic server certificate rotation helps you maintain high security standards while removing the operational burden of manual rotation.

For more information about enabling automatic server certificate rotation for your instance, see [Enable automatic server certificate rotation](https://docs.cloud.google.com/sql/docs/sqlserver/manage-ssl-instance#automatic-server-certificate-rotation-cas) .

## February 23, 2026

Feature

Gemini Cloud Assist investigation capabilities are now supported in Cloud SQL for SQL Server ([Preview](https://cloud.google.com/products#product-launch-stages)).

For more information, see [Troubleshoot slow queries with AI assistance](https://docs.cloud.google.com/sql/docs/sqlserver/monitor-troubleshoot-with-ai#troubleshoot-slow-queries).

## February 18, 2026

Deprecated

Control of MCP use with organization policies is deprecated. After March 17, 2026, organization policies that use the `gcp.managed.allowedMCPServices` constraint won't work, and you can control MCP use with IAM deny policies. For more information about controlling MCP use, see [Control MCP use with IAM](https://docs.cloud.google.com/mcp/control-mcp-use-iam).

Change

After March 17, 2026, when you enable the Cloud SQL Admin API (`sqladmin.googleapis.com`), the Cloud SQL remote MCP server is enabled automatically.

The Cloud SQL remote MCP server is in [Preview](https://cloud.google.com/products#product-launch-stages).

## February 17, 2026

Announcement

New best practices are available for securing generative AI agents using Model Context Protocol (MCP) with Google Cloud databases. This guide covers key security measures like least privilege, native database controls, and secure agent design to help you build safer AI applications. For more information, see [Best practices for securing agent interactions with Model Context Protocol](https://docs.cloud.google.com/sql/docs/sqlserver/secure-agent-interactions-mcp) .

## February 09, 2026

Feature

You can now use the [Cloud SQL remote MCP server](https://docs.cloud.google.com/sql/docs/sqlserver/use-cloudsql-mcp) . The Cloud SQL remote MCP server lets you interact easily with Cloud SQL instances from LLMs, AI applications, and AI-enabled development platforms.

This feature is in [Preview](https://cloud.google.com/products#product-launch-stages).

## February 02, 2026

Feature

You can now update the server certificate authority (CA) mode of an existing Cloud SQL instance. You can update existing instances that use the per-instance CA option (`GOOGLE_MANAGED_INTERNAL_CA`) to use the shared CA option (`GOOGLE_MANAGED_CAS_CA`) or the customer-managed CA option (`CUSTOMER_MANAGED_CAS_CA`).

For more information about the different server CA mode options, see [Certificate authority (CA) hierarchies](https://docs.cloud.google.com/sql/docs/sqlserver/authorize-ssl#ca-hierarchies).

## December 16, 2025

Feature

Cloud SQL enhanced backups are now generally available ([GA](https://cloud.google.com/products#product-launch-stages)).

With enhanced backups, backups are managed and stored in a centralized backup management project that leverages the [Backup and DR service](https://docs.cloud.google.com/backup-disaster-recovery/docs), and provides enforced retention, granular scheduling, and longer retention.

Enhanced backups now also support [point-in-time-recovery (PITR) after instance deletion](https://docs.cloud.google.com/sql/docs/sqlserver/backup-recovery/restore).

For more information about the available options and their limitations, see [Backup options](https://docs.cloud.google.com/sql/docs/sqlserver/backup-recovery/backup-options). For more information about enhanced backups pricing, see [Backup and DR pricing](https://cloud.google.com/backup-disaster-recovery/pricing).

## December 11, 2025

Feature

[Cloud SQL for SQL Server integration with Microsoft Entra ID](https://docs.cloud.google.com/sql/docs/sqlserver/integration-with-microsoft-entra-id) ([Preview](https://cloud.google.com/products#product-launch-stages)) provides centralized identity and access management (IAM) for your databases using your existing Microsoft Entra ID tenant.

## October 29, 2025

Feature

You can integrate Cloud SQL for SQL Server with customer-managed Active Directory (CMAD).

CMAD provides capabilities such as authentication and authorization. Joining an instance to a CMAD domain lets you sign in using Windows Authentication with an AD-based identity.

[Customer-managed Active Directory (CMAD)](https://docs.cloud.google.com/sql/docs/sqlserver/cmad) is [generally available](https://cloud.google.com/products#product-launch-stages) (GA).

## October 17, 2025

Feature

Cloud SQL Enterprise edition now supports a new machine series called the N4 machine series. This machine series provides balanced price-to-performance and uses the Hyperdisk Balanced storage. You can create custom machine types for the N4 machine series with up to 80 vCPUs and up to 640 GB memory. The N4 machine series is [generally available](https://cloud.google.com/products#product-launch-stages) (GA).

For more information about the N4 machine series and its availability, see [Machine series overview](https://docs.cloud.google.com/sql/docs/sqlserver/machine-series-overview).

## October 06, 2025

Feature

You can now use [advanced disaster recovery (DR)](https://docs.cloud.google.com/sql/docs/sqlserver/intro-to-cloud-sql-disaster-recovery#advanced-dr) for your Private Service Connect (PSC) enabled Cloud SQL Enterprise Plus edition instances. With advanced DR, you can: 

  * Designate a cross-region disaster recovery (DR) replica
  * Perform a cross-region replica failover for disaster recovery
  * Restore your original deployment by using zero-data loss switchover

You can also use switchover to simulate disaster recovery without data loss. For more information, see [Use advanced disaster recovery (DR)](https://docs.cloud.google.com/sql/docs/sqlserver/use-advanced-disaster-recovery). This feature is [generally available](https://cloud.google.com/products#product-launch-stages) (GA).

## September 29, 2025

Feature

You can now [use Gemini's capabilities to fix errors in a query within Cloud SQL Studio](https://docs.cloud.google.com/sql/docs/sqlserver/write-sql-gemini#fix-query) ([Preview](https://cloud.google.com/products#product-launch-stages)).

## September 23, 2025

Feature

You can now provision, manage and query your databases using the dedicated Gemini CLI extension for Cloud SQL for SQL Server. The extension provides full lifecycle control of your database—from provisioning instances, to exploring schemas and troubleshooting issues—from your command-line interface. 

For more information, see [Use Cloud SQL for SQL Server with MCP, Gemini CLI, and other agents](https://docs.cloud.google.com/sql/docs/sqlserver/pre-built-tools-with-mcp-toolbox).

Feature

You can now retain point-in-time recovery (PITR) logs for an instance after its deletion for a specified retention period. These logs can be used to restore the deleted instance to a specific point in time. For more information, see [Restore a deleted instance using PITR](https://docs.cloud.google.com/sql/docs/sqlserver/backup-recovery/restore#deleted-instance).

## September 08, 2025

Feature

You can have Cloud SQL create a [Private Service Connect](https://docs.cloud.google.com/sql/docs/sqlserver/about-private-service-connect#psc-endpoint) endpoint automatically. You can use this endpoint to access Cloud SQL instances through a VPC network. For more information, see [Create a Private Service Connect endpoint automatically](https://docs.cloud.google.com/sql/docs/sqlserver/configure-private-service-connect#create-endpoint-automatically). 

This feature is now generally available ([GA](https://cloud.google.com/products#product-launch-stages)).

## September 03, 2025

Feature

You can now enable your instance to take a final backup at instance deletion and define its retention period by setting the final backup [instance setting](https://docs.cloud.google.com/sql/docs/sqlserver/instance-settings). 

You can also create a [custom organization policy](https://docs.cloud.google.com/sql/docs/sqlserver/org-policy/custom-org-policy) to define final backup instance settings. For more information, see [Final backup](https://docs.cloud.google.com/sql/docs/sqlserver/backup-recovery/backups#final-backup).

## August 29, 2025

Feature

[`Max degree of parallelism (MAXDOP)`](https://docs.cloud.google.com/sql/docs/sqlserver/flags#max-degree-of-parallelism) is a Microsoft database flag available for use in Cloud SQL for SQL Server. This flag lets you limit the maximum number of threads used when running a single query in a parallel plan.

## August 21, 2025

Feature

You can save and manage SQL queries in Cloud SQL Studio. This feature is in [Preview](https://cloud.google.com/products#product-launch-stages). For more information, see [Saved queries overview](https://docs.cloud.google.com/sql/docs/sqlserver/saved-queries).

## August 15, 2025

Feature

Now you can create an IPv6 endpoint for Private Service Connect (PSC) connections. For more information, see [Connect to an instance using Private Service Connect](https://docs.cloud.google.com/sql/docs/sqlserver/configure-private-service-connect#create-psc-endpoint).

Feature

Now you can use [Private Service Connect backends](https://docs.cloud.google.com/sql/docs/sqlserver/about-private-service-connect#psc-backend), as an alternative to Private Service Connect endpoints, to access Cloud SQL instances.

Deprecated

You can no longer set a deny maintenance period for instances that are running a maintenance version older than 12 months. To update your instance, [perform self-service maintenance](https://docs.cloud.google.com/sql/docs/sqlserver/self-service-maintenance) or wait until the [next maintenance window](https://docs.cloud.google.com/sql/docs/sqlserver/set-maintenance-window#find-maintenance-api) to update your instance automatically. For more information about maintenance, see [Maintenance updates on Cloud SQL instances](https://docs.cloud.google.com/sql/docs/sqlserver/maintenance).

## August 13, 2025

Feature

Cloud SQL now supports Private Service Connect (PSC) outbound connectivity. With PSC outbound connectivity, you can attach a PSC interface to your existing Cloud SQL PSC-enabled instances to allow your instances to make outbound connections to your network. For more information, see [PSC outbound connections](https://docs.cloud.google.com/sql/docs/sqlserver/about-private-service-connect#psc-outbound).

## August 07, 2025

Feature

Cloud SQL now offers planned maintenance and machine tier upgrades for your Cloud SQL Enterprise plus instances with near-zero downtime for eligible instances.

For more information, see [Maintenance updates on Cloud SQL instances](https://docs.cloud.google.com/sql/docs/sqlserver/maintenance#nearzero).

## July 31, 2025

Feature

Cloud SQL now offers two options of backup services to manage your instance's backups:

  * **Enhanced backups** ([Preview](https://cloud.google.com/products#product-launch-stages)): backups are managed and stored in a centralized backup management project that leverages the [Backup and DR service](https://docs.cloud.google.com/backup-disaster-recovery), and provides enforced retention, granular scheduling, and longer retention.

  * **Standard backups** (existing option): backups are created, managed, and stored in the same project as your Cloud SQL instances. 




You can choose between these options based on your instance's requirements and needs. Although instances can't use both backup options at the same time, Cloud SQL gives you the ability to switch between these backup options as necessary. 

For more information about the available options and their limitations, see [Backup options](https://docs.cloud.google.com/sql/docs/sqlserver/backup-recovery/backups#backup-options).

## July 08, 2025

Feature

Cloud SQL for SQL Server now offers Active Directory support for write endpoints. For more information, see [Write endpoints across forests](https://docs.cloud.google.com/sql/docs/sqlserver/configure-private-ip#cross-forest-trusts).

## May 28, 2025

Feature

Cloud SQL for SQL Server now offers the maximum server memory recommender.

Database instances running with an allocation of memory that's either too low or too high might experience performance issues.

The `max server memory (mb)` flag limits the amount of memory that Cloud SQL can allocate for its internal pools. You can manually set a value for this flag, or omit the flag and let Cloud SQL manage memory limits for you automatically.

For more information, see [Optimize maximum server memory usage](https://docs.cloud.google.com/sql/docs/sqlserver/recommender-maximum-server-memory).

## May 23, 2025

Change

Cloud SQL for SQL Server now extends [query insights](https://docs.cloud.google.com/sql/docs/sqlserver/using-query-insights#query-insights-for-enterprise-plus) and [index advisor](https://docs.cloud.google.com/sql/docs/sqlserver/use-index-advisor#limitations) support to read replicas.

## May 22, 2025

Feature

You can now create an instance with both private services access and Private Service Connect enabled. You can also enable Private Service Connect on an existing private services access instance. This feature is now generally available ([GA](https://cloud.google.com/products#product-launch-stages)).

For more information, see [Configure both private services access and Private Service Connect](https://docs.cloud.google.com/sql/docs/sqlserver/configure-private-services-access-and-private-service-connect).

## May 14, 2025

Feature

Cloud SQL for SQL Server now supports [TLS connections](https://docs.cloud.google.com/sql/docs/sqlserver/ad#active_directory_endpoints_and_tls_connections) to Active Directory endpoints without requiring server certificate trust or the use of IP addresses. Existing [server certificates](https://docs.cloud.google.com/sql/docs/sqlserver/manage-ssl-instance) will need to be rotated to use this feature.

## May 08, 2025

Change

If you create an instance using the Google Cloud Console, then the per-instance CA (`GOOGLE_MANAGED_INTERNAL_CA`) option is now the default [server certificate authority (CA) mode](https://docs.cloud.google.com/sql/docs/sqlserver/authorize-ssl#ca-hierarchies) for your Cloud SQL instance.

For users of the [Cloud SQL Auth Proxy](https://docs.cloud.google.com/sql/docs/sqlserver/sql-proxy): 

  * If the Cloud SQL instance to which you're connecting is using [shared certificate authority (CA)](https://docs.cloud.google.com/sql/docs/sqlserver/authorize-ssl#shared-regional-ca) for its `serverCaMode` setting, then on the client side, you must use Cloud SQL Auth Proxy version 2.13.0 or later.
  * If the Cloud SQL instance to which you're connecting is using [customer-managed CA](https://docs.cloud.google.com/sql/docs/sqlserver/authorize-ssl#customer-managed-ca) for its `serverCaMode` setting, then on the client side, you must use Cloud SQL Auth Proxy version 2.14.3 or later.



## May 05, 2025

Feature

Cloud SQL for Enterprise Plus edition supports [AI-assisted troubleshooting](https://docs.cloud.google.com/sql/docs/sqlserver/observe-troubleshoot-with-ai). With AI-assisted troubleshooting, you can resolve complex database performance issues like [slow queries](https://docs.cloud.google.com/sql/docs/sqlserver/troubleshoot-slow-queries) and [high load](https://docs.cloud.google.com/sql/docs/sqlserver/troubleshoot-high-database-load) for your instances in a guided manner. To use AI-assisted troubleshooting, you need [Gemini Cloud Assist](https://docs.cloud.google.com/gemini/docs/cloud-assist/overview) and [query insights for Enterprise Plus edition](https://docs.cloud.google.com/sql/docs/sqlserver/using-query-insights#enable-insights). AI-assisted troubleshooting is available in [Preview](https://cloud.google.com/products#product-launch-stages).

## May 02, 2025

Feature

You can now [set up custom DNS names by configuring the custom subject alternative name (SAN)](https://docs.cloud.google.com/sql/docs/sqlserver/custom-dns-name) for your instance. After you set up DNS name resolution, you can connect to your Cloud SQL instance using the custom DNS name instead of using an IP address. This feature is available only for instances that are configured with the [customer-managed certificate authority (CA)](https://docs.cloud.google.com/sql/docs/sqlserver/customer-managed-ca) (`CUSTOMER_MANAGED_CAS_CA`) option as its server CA mode. 

Custom SAN configuration for instances is [generally available](https://cloud.google.com/products#product-launch-stages) (GA).

## May 01, 2025

Feature

Cloud SQL gives you the flexibility to choose between three [CA hierarchy options](https://docs.cloud.google.com/sql/docs/sqlserver/authorize-ssl#ca-hierarchies) when you [create a Cloud SQL instance](https://docs.cloud.google.com/sql/docs/sqlserver/create-instance).

You can choose between the per-instance CA (`GOOGLE_MANAGED_INTERNAL_CA`), the shared CA (`GOOGLE_MANAGED_CAS_CA`), or the customer-managed CA (`CUSTOMER_MANAGED_CAS_CA`) options as the server certificate authority (CA) mode for your instance. If you create an instance using the Google Cloud Console, then the shared CA option, (`GOOGLE_MANAGED_CAS_CA`), is the default configuration. If you create an instance using gcloud, the Cloud SQL Admin REST API, or Terraform, then the per-instance CA option (`GOOGLE_MANAGED_INTERNAL_CA`) is the default configuration.

The shared CA and customer-managed CA options are now [generally available](https://cloud.google.com/products#product-launch-stages) (GA).

## April 24, 2025

Feature

[Private Service Connect endpoint propagation](https://docs.cloud.google.com/sql/docs/sqlserver/about-private-service-connect#psc-endpoint-propagation) is now [generally available](https://cloud.google.com/products#product-launch-stages) (GA). You can use the Network Connectivity Center hub to propagate the Private Service Connect endpoints of your Cloud SQL instances in a VPC network.

## April 09, 2025

Feature

Query insights for Cloud SQL Enterprise edition and Cloud SQL Enterprise Plus edition is now generally available (GA) for Cloud SQL for SQL Server. You can also now view the query details, query plans, and statistical query execution charts for your top queries. 

For more information, see [Use query insights to improve query performance](https://docs.cloud.google.com/sql/docs/sqlserver/using-query-insights).

## April 07, 2025

Feature

Cloud SQL now supports the [Enterprise Plus recommender](https://docs.cloud.google.com/sql/docs/sqlserver/recommender-enterprise-plus). Based on your application workloads and resource utilization, the recommender helps you optimize performance by identifying SQL Server instances that might see performance improvements when upgraded to Cloud SQL Enterprise Plus edition.

## March 28, 2025

Feature

When you create a Cloud SQL for SQL Server instance, version [SQL Server 2022 Standard is now the default](https://docs.cloud.google.com/sql/docs/sqlserver/instance-settings).

## March 24, 2025

Feature

You can [export the transaction logs for all Cloud SQL for SQL Server instances that have point-in-time recovery (PITR) enabled and their logs stored in Cloud Storage](https://docs.cloud.google.com/sql/docs/sqlserver/import-export/import-export-bak#export-transaction-logs).

Feature

Cloud SQL now lets you retain existing backups after an instance is deleted. These consist of on-demand and automatic backups created when the instance was live. For more information, see [Retained backups](https://docs.cloud.google.com/sql/docs/sqlserver/backup-recovery/backups#retained-backups).

## March 17, 2025

Feature

Cloud SQL for SQL Server supports transparent data encryption (TDE) to encrypt data stored in your Cloud SQL for SQL Server instances. 

TDE automatically encrypts data before it is written to storage, and automatically decrypts data when the data is read from storage.

TDE provides another layer of encryption in addition to Google's default offering of encryption for data at rest and Google's optional offering of customer-managed encryption keys (CMEK). TDE helps you meet regulatory compliance requirements and supports import or export operations of TDE encrypted backups. For more information, see [About transparent data encryption](https://docs.cloud.google.com/sql/docs/sqlserver/about-tde).

## March 14, 2025

Feature

You can [use PITR to restore a Cloud SQL for SQL Server instance that isn't available](https://docs.cloud.google.com/sql/docs/sqlserver/backup-recovery/restore#pitr-instance-not-available).

## March 04, 2025

Feature

[Cloud SQL Enterprise edition](https://docs.cloud.google.com/sql/docs/sqlserver/instance-settings) now supports the `europe-north2` (Stockholm) region.

## February 20, 2025

Feature

You can now create a final backup of your data before you delete a Cloud SQL instance. You can use the final backup to restore your data to a new instance. This way, you can recover your data after you delete the instance. For more information, see [About Cloud SQL backups](https://docs.cloud.google.com/sql/docs/sqlserver/backup-recovery/backups#final-backups).

## February 14, 2025

Change

[Point in time recovery (PITR)](https://docs.cloud.google.com/sql/docs/sqlserver/backup-recovery/pitr) is available by default for all Cloud SQL Enterprise Plus edition for SQL Server instances.

## February 11, 2025

Feature

You can now use a custom DNS name to connect to your Cloud SQL instances by adding a custom subject alternative name (SAN) to your Cloud SQL instances. This feature is available for instances that are configured with Customer Managed CAS CA.. For more information, see [Create instances](https://docs.cloud.google.com/sql/docs/sqlserver/create-instance).

You can also add, modify, and remove a custom SAN for existing Cloud SQL instances. For more information, see [Edit instances](https://docs.cloud.google.com/sql/docs/sqlserver/edit-instance). 

This feature is available in [Preview](https://cloud.google.com/products#product-launch-stages).

## February 05, 2025

Feature

You can now configure customer-managed CA (`CUSTOMER_MANAGED_CAS_CA`) as the server certificate authority (CA) mode when you create a Cloud SQL instance. With customer-managed CA mode, you set up your own CA pool and CA in [Certificate Authority Service](https://docs.cloud.google.com/certificate-authority-service/docs/ca-service-overview). This option lets you establish your own CA hierarchy and manage the rotation of CA certificates for your Cloud SQL instances to help you meet your regulatory compliance needs. 

To use the customer-managed CA option in Cloud SQL, see [Use a customer-managed certificate authority (CA)](https://docs.cloud.google.com/sql/docs/sqlserver/customer-managed-ca). For more information about server CA mode options, see [Certificate authority (CA) hierarchies](https://docs.cloud.google.com/sql/docs/sqlserver/authorize-ssl#ca-hierarchies). The customer-managed CA feature is in [Preview](https://cloud.google.com/products#product-launch-stages).

## January 27, 2025

Change

Transaction logs associated with [point-in-time-recovery (PITR)](https://docs.cloud.google.com/sql/docs/sqlserver/backup-recovery/pitr) operations for all Cloud SQL for SQL Server instances are now stored in Cloud Storage. On May 31, 2024, Google Cloud launched support for PITR transaction log storage in Cloud Storage. Since then, Google Cloud has run a transparent migration of these transaction logs to Cloud Storage for all instances created prior to the launch date. This migration is now complete. 

**Note:** If your Cloud SQL for SQL Server instance is on the old network architecture, the transaction logs for PITR may still remain on disk until migrated to the new network architecture. To verify the storage of your instance's transaction logs for PITR, see [Check the storage location of transaction logs used for PITR](https://docs.cloud.google.com/sql/docs/sqlserver/backup-recovery/pitr#check-log-storage-location).

## January 17, 2025

Feature

Control the file size of the tempdb database. For more information, see [Manage a tempdb database](https://docs.cloud.google.com/sql/docs/sqlserver/managing-tempdb).

## December 20, 2024

Feature

You can use the following observability dashboards in Cloud SQL for SQL Server to monitor, analyze, and diagnose issues with your instances, databases, and queries:

  * System insights
  * Query insights



Both of these dashboards are available to you in the Google Cloud Console. The System insights dashboard displays the metrics for the resources that your instance is using and can help you analyze the performance of your instance. For more information, see [Use system insights to improve system performance](https://docs.cloud.google.com/sql/docs/sqlserver/use-system-insights). System insights is [generally available](https://cloud.google.com/products#product-launch-stages) (GA).

The Query insights dashboard helps you detect problems with queries in your Cloud SQL databases. The dashboard also provides you with the ability to [monitor active queries](https://docs.cloud.google.com/sql/docs/sqlserver/monitor-active-queries) and view [index advisor](https://docs.cloud.google.com/sql/docs/sqlserver/index-advisor-overview) recommendations. For more information, see [Use query insights to improve query performance](https://docs.cloud.google.com/sql/docs/sqlserver/using-query-insights). Query insights for Cloud SQL for SQL Server is in [Preview](https://cloud.google.com/products#product-launch-stages).

You can enable [query insights for Cloud SQL Enterprise Plus edition](https://docs.cloud.google.com/sql/docs/sqlserver/using-query-insights#query-insights-for-enterprise-plus). When you enable query insights for Enterprise Plus, you can access additional features in query insights such as 30 days of metrics retention, granular query plan details, and a higher query length limit. The query insights for Cloud SQL Enterprise Plus edition, index advisor, and active queries features are also in [Preview](https://cloud.google.com/products#product-launch-stages).

## December 10, 2024

Change

Cloud SQL now offers notifications for maintenance that's either started or completed. See the [Overview of maintenance on Cloud SQL](https://docs.cloud.google.com/sql/docs/sqlserver/maintenance#notifications) instances. To find out how to sign up for notifications and check your instances for upcoming maintenance, see [Find and set maintenance windows](https://docs.cloud.google.com/sql/docs/sqlserver/set-maintenance-window).

## December 05, 2024

Feature

[Cloud SQL Enterprise Plus edition](https://docs.cloud.google.com/sql/docs/editions-intro) now supports the following regions:

  * `africa-south1` (Johannesburg)
  * `asia-east2` (Hong Kong)
  * `europe-west10` (Berlin)



## December 03, 2024

Feature

You can now use the Network Connectivity Center hub to [propagate Private Service Connect endpoints](https://docs.cloud.google.com/sql/docs/sqlserver/about-private-service-connect#psc-endpoint-propagation) of Cloud SQL instances in a VPC network. All endpoints in this network become accessible transitively to other spoke VPC networks through the hub. This feature is available in [Preview](https://cloud.google.com/products#product-launch-stages).

## November 27, 2024

Feature

You can now create instances with both private services access and Private Service Connect enabled for them. You can also enable Private Service Connect for existing private services access instances. This feature is available in [Preview](https://cloud.google.com/products#product-launch-stages). For more information, see [Configure both private services access and Private Service Connect](https://docs.cloud.google.com/sql/docs/sqlserver/configure-private-services-access-and-private-service-connect).

## November 18, 2024

Feature

Support for the [`northamerica-south1`](https://docs.cloud.google.com/sql/docs/sqlserver/locations) (Mexico) region.

## November 14, 2024

Feature

You can now create custom organization policies for the [`BackupRun`](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest/v1/backupRuns) resource in Cloud SQL instances. In addition, more fields in the [`Instances`](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest/v1/instances) resource are available to create custom organization policies. For more information, see [Add custom organization policies](https://docs.cloud.google.com/sql/docs/sqlserver/org-policy/custom-org-policy).

## November 12, 2024

Feature

You can now have Cloud SQL create a Private Service Connect endpoint automatically instead of creating the endpoint manually after the instance is created. You use this endpoint to access a Cloud SQL instance through a VPC network. For more information, see [Connect to an instance using Private Service Connect](https://docs.cloud.google.com/sql/docs/sqlserver/configure-private-service-connect#create-endpoint-automatically). This feature is available in [Preview](https://cloud.google.com/products#product-launch-stages).

## November 04, 2024

Feature

You can now [view the size of a backup](https://docs.cloud.google.com/sql/docs/sqlserver/backup-recovery/backing-up#view-backup-size) for a Cloud SQL instance.

## October 25, 2024

Feature

When you run the [`backupRuns.GET` API](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest/v1/backupRuns/get) or the [`gcloud sql backups describe`](https://docs.cloud.google.com/sdk/gcloud/reference/sql/backups/describe) command, the `maxChargeableBytes` parameter now appears in the response. This parameter contains the maximum number of bytes that you can be charged for a backup.

## October 21, 2024

Feature

You can now create a read replica for an instance that has [private services access](https://docs.cloud.google.com/sql/docs/sqlserver/configure-private-services-access#configure-access) configured for it and [connector enforcement](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest/v1/instances#ConnectorEnforcement) enabled for it. For more information, see [Connect using Cloud SQL Language Connectors](https://docs.cloud.google.com/sql/docs/sqlserver/connect-connectors#enforce).

## October 09, 2024

Feature

You can [export the transaction logs](https://docs.cloud.google.com/sql/docs/sqlserver/import-export/import-export-bak) for point-in-time recovery (PITR) that Cloud SQL stores in Cloud Storage. This feature is in [Preview](https://cloud.google.com/products#product-launch-stages).

Feature

Cloud SQL configures the `max server memory (mb)` flag based on the instance size automatically by limiting the amount of memory that SQL Server can allocate for its internal pools. For more information, see [Configure database flags](https://docs.cloud.google.com/sql/docs/sqlserver/flags).

## October 03, 2024

Feature

You can now configure server certificate authority (CA) mode when you create a Cloud SQL instance. With server CA mode, you have two options:

  * **Per-instance CA** : this is the default configuration. With this option, an internal CA dedicated to each Cloud SQL instance signs the server certificate for that instance.
  * **Shared CA** : with this option, the Cloud SQL instance uses a CA hierarchy consisting of a root CA and subordinate server CAs managed by Cloud SQL and hosted on Google Cloud Certificate Authority Service (CA Service). The subordinate server CAs in a region sign the server certificates and are shared across instances in the region.



For more information about each option, see [Certificate authority (CA) hierarchies](https://docs.cloud.google.com/sql/docs/sqlserver/authorize-ssl#certificate_authority_ca_hierarchies). This feature is in [Preview](https://cloud.google.com/products#product-launch-stages).

## October 01, 2024

Feature

You can now use the `gcloud sql instances patch` command to update the time zone of your Cloud SQL for SQL Server instance after you create the instance. Previously, you could only set a custom time zone for a SQL Server instance when you first created the instance. For more information about setting the time zone for a Cloud SQL for SQL Server instance, see [About instance settings](https://docs.cloud.google.com/sql/docs/sqlserver/instance-settings#timezone).

## September 13, 2024

Feature

For Cloud SQL Enterprise Plus edition, you can set the number of days of retained transaction logs from 1 to 35. For more information, see [Use point-in-time recovery (PITR)](https://docs.cloud.google.com/sql/docs/sqlserver/backup-recovery/pitr).

## September 12, 2024

Feature

You can now provide access to Cloud SQL Studio by granting a new IAM role, Cloud SQL Studio User (`roles/cloudsql.studioUser`), instead of using the Cloud SQL Admin IAM role.

For more information about using Cloud SQL Studio, see [Manage your data using Cloud SQL Studio](https://docs.cloud.google.com/sql/docs/sqlserver/manage-data-using-studio).

## September 03, 2024

Feature

When you clone your zonal instance, you can now specify a preferred zone for the instance. You can also specify preferred primary and secondary zones for your regional instance. If the zones for your instance go down in the future, then Cloud SQL can assign the preferred zones to the instance, and you don't experience downtime. For more information, see [Clone instances](https://docs.cloud.google.com/sql/docs/sqlserver/clone-instance).

## August 01, 2024

Feature

Cloud SQL for SQL Server now offers two editions of Cloud SQL to support your various business and application needs: **Cloud SQL Enterprise Plus edition** and **Cloud SQL Enterprise edition**. Each edition provides different performance and availability characteristics to meet the needs of your applications.

Cloud SQL Enterprise Plus edition has new machines for better performance, higher availability, and advanced disaster recovery. Existing instances become Cloud SQL Enterprise edition for SQL Server instances with no changes to pricing or features. You can upgrade existing instances to the Cloud SQL Enterprise Plus edition in-place using the Google Cloud Console, the gcloud CLI, or the API with minimal downtime.

For more information about Cloud SQL editions, see [Introduction to Cloud SQL editions](https://docs.cloud.google.com/sql/docs/editions-intro).

## July 25, 2024

Change

You can now upgrade the network architecture of a Cloud SQL instance that isn't enabled with [high-availability](https://docs.cloud.google.com/sql/docs/sqlserver/high-availability). The previous limitation on upgrading the network architecture of these instances is removed. To check whether your Cloud SQL instance has high availability enabled, see [Verify an instance's high availability configuration](https://docs.cloud.google.com/sql/docs/sqlserver/configure-ha#verify-ha).

For more information about upgrading your network architecture, see [Upgrade an instance to the new network architecture](https://docs.cloud.google.com/sql/docs/sqlserver/upgrade-cloud-sql-instance-new-network-architecture).

## July 19, 2024

Feature

You can now use [Extended Events (XEvents)](https://docs.cloud.google.com/sql/docs/sqlserver/extended-events) on your Cloud SQL for SQL Server instance to monitor, identify, and troubleshoot the performance of the databases on your instance.

## July 18, 2024

Feature

You can now create custom organization policies for Cloud SQL instances. For more information, see [Add custom organization policies](https://docs.cloud.google.com/sql/docs/sqlserver/org-policy/custom-org-policy).

## July 16, 2024

Feature

Cloud SQL Studio is now [generally available](https://cloud.google.com/products#product-launch-stages). For more information, see [Manage your data using Cloud SQL Studio](https://docs.cloud.google.com/sql/docs/sqlserver/manage-data-using-studio).

Feature

You can now search for and manage your Cloud SQL resources by using [Dataplex Catalog](https://docs.cloud.google.com/dataplex/docs/catalog-overview). For more information about the integration of Cloud SQL and Dataplex Catalog, see [Manage your Cloud SQL resources using Dataplex Catalog](https://docs.cloud.google.com/sql/docs/sqlserver/dataplex-catalog-integration).

## June 20, 2024

Feature

You can now use the `gcloud sql instances describe` command or the SQL Admin API to retrieve a list of database versions that are available to your SQL Server instance for upgrade. For more information, see [Plan a major version upgrade](https://docs.cloud.google.com/sql/docs/sqlserver/upgrade-major-db-version-inplace#plan-upgrade).

## June 10, 2024

Feature

You can now choose to receive a maintenance notification 5 weeks before the maintenance update of your Cloud SQL instance is scheduled to occur. This option is named **Week 5**.

In addition, some labels in the Google Cloud Console have been renamed to align with this new option:

  * **Order of update** is renamed to **Maintenance timing**
  * **Earlier** is renamed to **Week 1**
  * **Later** is renamed to **Week 2**



For more information, see [Maintenance settings](https://docs.cloud.google.com/sql/docs/sqlserver/maintenance#management) and [Find and set maintenance windows](https://docs.cloud.google.com/sql/docs/sqlserver/set-maintenance-window).

## May 31, 2024

Feature

Cloud SQL for SQL Server now supports storage of [point-in-time recovery (PITR)](https://docs.cloud.google.com/sql/docs/sqlserver/backup-recovery/restore#tips-pitr) transaction logs in Cloud Storage.

## April 09, 2024

Feature

The following [Gemini in Databases](https://docs.cloud.google.com/gemini/docs/databases/overview) features are now available in Public Preview:

  * [Database Center](https://docs.cloud.google.com/database-center/docs/overview): an AI-assisted dashboard that gives you one centralized view across your entire database fleet.
  * [Cloud SQL Studio](https://docs.cloud.google.com/sql/docs/sqlserver/manage-data-using-studio): lets authorized users interact directly with the SQL database and run SQL queries from the Google Cloud console to access and manipulate data.
  * 9 new database insight recommendations.



To learn how to enable and activate Gemini in Databases, see [Set up Gemini in Databases](https://docs.cloud.google.com/gemini/docs/databases/set-up-gemini).

## April 02, 2024

Feature

You can now use SSL mode instead of the legacy `require_ssl` setting to specify the encryption requirements for connections to your Cloud SQL for SQL Server instances. For more information, see [Enforce SSL/TLS encryption](https://docs.cloud.google.com/sql/docs/sqlserver/configure-ssl-instance#enforcing-ssl).

## March 25, 2024

Feature

You can now use [Private Service Connect](https://docs.cloud.google.com/sql/docs/sqlserver/configure-private-service-connect) to connect to a Cloud SQL for SQL Server instance. This solution allows you to connect to the instance from multiple VPC networks that belong to different groups, teams, projects, or organizations.

Private Service Connect includes support for [cross-region read replicas](https://docs.cloud.google.com/sql/docs/sqlserver/replication/create-replica#create-read-replica-cloud-sql-instance-psc-enabled). You can also [choose an availability type](https://docs.cloud.google.com/sql/docs/sqlserver/configure-ha) (REGIONAL or ZONAL) for Private Service Connect-enabled instances. 

All features are in [GA](https://cloud.google.com/products#product-launch-stages).

## March 14, 2024

Announcement

A new maintenance version rollout is currently underway for all supported SQL Server versions.

If you have configured a maintenance window for your instance, then the updates will occur according to the timeframe that you set in the window. Otherwise, the updates will occur within the next few weeks. The new maintenance version is [SQL Server version].R20240216.01_RC00.

To learn how to check your maintenance version, see [Self-service maintenance](https://docs.cloud.google.com/sql/docs/sqlserver/self-service-maintenance#before-you-begin). To find your maintenance window or to manage maintenance updates, see [Find and set maintenance windows](https://docs.cloud.google.com/sql/docs/sqlserver/set-maintenance-window).

## March 13, 2024

Feature

Cloud SQL now supports SQL Server Reporting Services (SSRS) on your instances. For more information, see [Use SSRS for creating reports](https://docs.cloud.google.com/sql/docs/sqlserver/ssrs).

## March 05, 2024

Feature

You can now upgrade your Cloud SQL instances to use the new network architecture to get additional capabilities not available in the old network architecture. For more information, see [Upgrade an instance to the new network architecture](https://docs.cloud.google.com/sql/docs/sqlserver/upgrade-cloud-sql-instance-new-network-architecture).

## February 09, 2024

Feature

Cloud SQL now automatically updates your read replicas when you perform self-service maintenance on the primary instance. For more information, see [Self-service maintenance](https://docs.cloud.google.com/sql/docs/sqlserver/self-service-maintenance).

## February 01, 2024

Feature

You can now use Private Service Connect to connect to a Cloud SQL for SQL Server instance. This solution allows you to connect to the instance from multiple VPC networks that belong to different groups, teams, projects, or organizations. 

You can also choose an availability type (REGIONAL or ZONAL) for Private Service Connect-enabled instances. 

All features are in [Preview](https://cloud.google.com/products#product-launch-stages). For more information, see [Connect to an instance using Private Service Connect](https://docs.cloud.google.com/sql/docs/sqlserver/configure-private-service-connect).

## January 31, 2024

Feature

Support for [africa-south1](https://docs.cloud.google.com/sql/docs/sqlserver/locations) (Johannesburg) region.

## November 15, 2023

Feature

Cloud SQL supports the bulk insert functionality of SQL Server for importing data. This functionality is supported only on SQL Server 2022.

For more information, see [Use bulk insert for importing data](https://docs.cloud.google.com/sql/docs/sqlserver/import-export#bulk-insert).

## October 17, 2023

Feature

You can now [import transaction log backups](https://docs.cloud.google.com/sql/docs/sqlserver/import-export/import-export-bak#import_transaction_log_backups). This can help you reduce downtime when migrating to Cloud SQL using backups.

## October 09, 2023

Deprecated

The [`cross db ownership chaining`](https://docs.cloud.google.com/sql/docs/sqlserver/flags#cross-db-ownership-chaining) flag is deprecated for all SQL Server versions. 

For cross-database access, use the [Microsoft tutorial for signing stored procedures with a certificate](https://learn.microsoft.com/en-us/sql/relational-databases/tutorial-signing-stored-procedures-with-a-certificate?view=sql-server-ver16).

## September 26, 2023

Feature

Cloud SQL supports the preview version of the enable-high-availability recommender. This service proactively generates recommendations that help you bring your important instances within SLA by providing data redundancy. This might be helpful during a zonal outage or when an instance runs out of memory. For more information, see [Improve instance reliability by enabling high availability](https://docs.cloud.google.com/sql/docs/sqlserver/recommender-enable-ha).

## September 19, 2023

Feature

Support for [me-central2 (Dammam)](https://docs.cloud.google.com/sql/docs/sqlserver/locations) region.

## August 22, 2023

Feature

Support for [europe-west10 (Berlin)](https://docs.cloud.google.com/sql/docs/sqlserver/locations) region.

## August 17, 2023

Feature

You can now [re-encrypt an existing Cloud SQL CMEK-enabled primary instance or replica](https://docs.cloud.google.com/sql/docs/sqlserver/configure-cmek#reencrypt) with a new primary key version.

## August 03, 2023

Feature

Cloud SQL now supports multiple categories of API rate quotas. Rate quotas for each category are imposed per minute, per project, per region, and per user. For more information about rate quotas for each category, see [Quotas and limits](https://docs.cloud.google.com/sql/docs/sqlserver/quotas).

Feature

The [Cloud SQL Node.js Language Connector](https://docs.cloud.google.com/static/sql/docs/sqlserver/connect-connectors#node.js) is now available for public preview.

## July 18, 2023

Feature

Cloud SQL now supports [default maintenance windows](https://docs.cloud.google.com/sql/docs/sqlserver/maintenance#default-windows) for your instances. With this release, an instance without a user-specified maintenance window is maintained outside of the typical business hours for the time zone that the instance is deployed in.

## July 06, 2023

Feature

Cloud SQL now supports [non-RFC 1918 IP address ranges](https://docs.cloud.google.com/sql/docs/sqlserver/configure-private-ip#non-rfc1918), including privately used public IP addresses. This enables you to create instances and replicas in a non-RFC 1918 IP address range. Additionally, you can connect to an instance from an application that is running in a non-RFC 1918 IP address range.

## June 26, 2023

Feature

Cloud SQL now supports SQL Server 2022. The default version continues to be SQL Server 2019 Standard. For more information, see [Database versions and version policies](https://docs.cloud.google.com/sql/docs/sqlserver/db-versions).

## June 07, 2023

Feature

You can now [import and export differential database backups](https://docs.cloud.google.com/sql/docs/sqlserver/import-export/import-export-bak). This can help you import and export data more frequently, reducing migration downtime.

## June 02, 2023

Security

A vulnerability was recently discovered in Cloud SQL for SQL Server that allowed customer administrator accounts to create triggers in the `tempdb` database and use those to gain `sysadmin` privileges in the instance. The `sysadmin` privileges would give the attacker access to system databases and partial access to the machine running that SQL Server instance.

Google Cloud resolved the issue by patching the security vulnerability by March 1, 2023. Google Cloud didn't find any compromised customer instances.

For instructions and more details, see the [Cloud SQL security bulletin](https://docs.cloud.google.com/sql/docs/security-bulletins#gcp-2023-007).

## May 16, 2023

Feature

The Cloud SQL Proxy Operator is now generally available. To learn more about the Cloud SQL Proxy Operator, see [About the Cloud SQL Proxy Operator](https://docs.cloud.google.com/sql/docs/mysql/connect-proxy-operator).

## May 15, 2023

Feature

You can now use the point-in-time-recovery (PITR) feature and read replicas on the same primary instance. For more information, see [Point-in-time Recovery](https://docs.cloud.google.com/sql/docs/sqlserver/backup-recovery/restore).

## May 02, 2023

Feature

You can now disable [simultaneous multithreading (SMT)](https://docs.cloud.google.com/sql/docs/sqlserver/create-instance#smt-create-instance) while creating or editing instances and read replicas. This might reduce your SQL Server licensing fees. To understand the impact of disabling SMT on your instance's performance, we recommend that you [perform load testing](https://docs.cloud.google.com/compute/docs/tutorials/load-testing-sql-server-hammerdb) on your instance.

## March 30, 2023

Feature

Support for [me-central1](https://docs.cloud.google.com/sql/docs/mysql/locations) (Doha) region.

Feature

Cloud SQL supports the [bcp utility of SQL Server for importing and exporting data](https://docs.cloud.google.com/sql/docs/sqlserver/import-export#use-bcp).

Feature

Cloud SQL supports the [SqlPackage utility of SQL Server for importing and exporting data](https://docs.cloud.google.com/sql/docs/sqlserver/import-export#use-sqlpackage).

## March 28, 2023

Feature

The changes in the September 15, 2022 Release Notes entry for read replica maintenance are now available. Cloud SQL read replicas follow the [maintenance settings](https://docs.cloud.google.com/sql/docs/sqlserver/maintenance#management) for the primary instance, including the maintenance window, rescheduling, and the deny maintenance period. During the maintenance event, Cloud SQL maintains the replicas before maintaining the primary instance. For more information, see [How does maintenance affect read replicas?](https://docs.cloud.google.com/sql/docs/sqlserver/maintenance#read-replicas)

Feature

Cloud SQL now exposes 38 new metrics. These metrics improve observability of Cloud SQL for SQL Server instances, helping you investigate performance issues and resource bottlenecks. You can find these metrics in the [Metrics explorer](https://docs.cloud.google.com/monitoring/charts/metrics-explorer) within the Monitoring dashboard.

For more information about these metrics, see [Cloud SQL Metrics](https://docs.cloud.google.com/monitoring/api/metrics_gcp#gcp-cloudsql).

## March 27, 2023

Feature

Cloud SQL now supports the Linked Servers functionality of SQL Server. You can use this capability to integrate data from multiple sources and distribute queries across multiple servers. To learn more, see [About linked servers](https://docs.cloud.google.com/sql/docs/sqlserver/linked-servers).

Feature

The Cloud SQL [Active Directory (AD) Diagnosis tool](https://docs.cloud.google.com/sql/docs/sqlserver/ad-diagnosis-tool) helps you troubleshoot issues that you might face while connecting to AD-enabled Cloud SQL for SQL Server instances, using an on-premises AD domain.

## March 23, 2023

Feature

Support for [europe-west12](https://docs.cloud.google.com/sql/docs/mysql/locations) (Turin) region.

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

Cloud SQL supports the preview version of the [Underprovisioned instance recommender](https://docs.cloud.google.com/sql/docs/sqlserver/recommender-underprovisioned). This service helps you avoid bottlenecks from high CPU and memory usage and minimize the likelihood of out-of-memory events. It gives you recommendations to resize your instances to a machine tier that better suits your workload.

## January 18, 2023

Feature

Cloud SQL for SQL Server enables you to [use point-in-time recovery](https://docs.cloud.google.com/sql/docs/sqlserver/backup-recovery/restore#tips-pitr).

Point-in-time recovery helps you recover an instance to a specific point in time. For example, if an error causes a loss of data, you can recover a database to its state before the error occurred. This feature is [generally available](https://docs.cloud.google.com/sql/docs/sqlserver/backup-recovery/pitr).

Feature

Cloud SQL now supports [viewing an audit log for an automated backup of an instance](https://docs.cloud.google.com/sql/docs/sqlserver/backup-recovery/view-audit-logs-for-automated-backups) to verify whether the backup is completed successfully. You can also configure a log-based alert so that a user can be notified of the backup's status.

## January 10, 2023

Feature

You can use [striped import](https://docs.cloud.google.com/sql/docs/sqlserver/import-export/import-export-bak#use-striped-import) and [striped export](https://docs.cloud.google.com/sql/docs/sqlserver/import-export/import-export-bak#use-striped-export) to reduce the time needed for BAK file operations and for other purposes. This feature is generally available.

## October 28, 2022

Change

The changes listed in the [September 15 Release Notes entry](https://docs.cloud.google.com/sql/docs/release-notes#September_15_2022) for read replica maintenance have been postponed.

## October 07, 2022

Feature

When you [create an instance](https://docs.cloud.google.com/sql/docs/sqlserver/create-instance), you can set a permanent time zone for the instance. This feature is [generally available](https://docs.cloud.google.com/sql/docs/sqlserver/instance-settings#timezone).

## October 04, 2022

Feature

Terraform is supported when you use [self-service maintenance](https://docs.cloud.google.com/sql/docs/mysql/self-service-maintenance#update-maintenance-version).

## September 21, 2022

Feature

Cloud SQL allows the re-use of an instance name immediately after the instance is deleted. For more information, see the [Cloud SQL for SQL Server FAQ](https://docs.cloud.google.com/sql/docs/sqlserver/faq#reuse).

## September 15, 2022

Feature

Cloud SQL read replicas now follow the [maintenance settings](https://docs.cloud.google.com/sql/docs/sqlserver/maintenance#management) for the primary instance, including the maintenance window, rescheduling, and the deny maintenance period. During the maintenance event, Cloud SQL maintains the replicas before maintaining the primary instance. For more information, see [How does maintenance affect read replicas?](https://docs.cloud.google.com/sql/docs/sqlserver/maintenance#read-replicas)

## September 13, 2022

Feature

Support for me-west1 (Tel Aviv).

## August 22, 2022

Change

Cloud SQL may set a value for the `max server memory (mb)` flag on instances, based on [Microsoft's recommended values](https://docs.microsoft.com/en-us/sql/database-engine/configure-windows/server-memory-server-configuration-options?view=sql-server-ver15#recommendations). For information about flags supported by Cloud SQL, see [Configure database flags](https://docs.cloud.google.com/sql/docs/sqlserver/flags#list-flags-sqlserver).

## August 15, 2022

Feature

By enabling instance deletion protection, you can prevent the accidental removal of Cloud SQL instances. This functionality is generally available.

For more information, see [Prevent deletion of an instance](https://docs.cloud.google.com/sql/docs/mysql/deletion-protection).

## July 11, 2022

Feature

The database major version upgrade feature of Cloud SQL for SQL Server is generally available. For more information, see [Upgrade the database major version in-place](https://docs.cloud.google.com/sql/docs/sqlserver/upgrade-major-db-version-inplace).

## July 08, 2022

Feature

The July maintenance changelog is now available. For more information, use the links at [Maintenance changelog](https://docs.cloud.google.com/sql/docs/sqlserver/maintenance-changelog).

## June 28, 2022

Feature

A second June maintenance changelog is now available. For more information, use the links at [Maintenance changelog](https://docs.cloud.google.com/sql/docs/sqlserver/maintenance-changelog).

## June 21, 2022

Feature

You can enable an instance to publish to a subscriber that is external (or internal) to Cloud SQL. In this scenario, Cloud SQL for SQL Server can act as a publisher to an external subscriber. This functionality, which is generally available, uses transactional replication. 

For more information, see [Configure external replicas](https://docs.cloud.google.com/sql/docs/sqlserver/replication/configure-external-replica).

Feature

In Cloud SQL, you can use SQL Server Audit capabilities to track and log server-level and database-level events. This functionality is generally available.

For more information, see [SQL Server database auditing](https://docs.cloud.google.com/sql/docs/sqlserver/db-audit).

## June 10, 2022

Feature

Cloud SQL now supports faster machine type changes, with connectivity dropping to less than 60 seconds. For more information, see [Impact of changing instance settings](https://docs.cloud.google.com/sql/docs/sqlserver/instance-settings#impact).

## June 09, 2022

Feature

The June maintenance changelog is now available. For more information, use the links at [Maintenance changelog](https://docs.cloud.google.com/sql/docs/sqlserver/maintenance-changelog).

## June 08, 2022

Feature

An addendum to the May maintenance changelog shows additional security patches. For more information, use the links at [Maintenance changelog](https://docs.cloud.google.com/sql/docs/sqlserver/maintenance-changelog).

## June 07, 2022

Feature

Support for us-south1 (Dallas).

## May 24, 2022

Feature

Support for us-east5 (Columbus).

## May 13, 2022

Feature

New maintenance versions are now available through [self-service maintenance](https://docs.cloud.google.com/sql/docs/sqlserver/self-service-maintenance). See the [maintenance changelog](https://docs.cloud.google.com/sql/docs/sqlserver/maintenance-changelog) to learn more about these new maintenance versions.

## May 04, 2022

Feature

Support for europe-west9 (Paris).

## May 02, 2022

Feature

New maintenance versions are now available through [self-service maintenance](https://docs.cloud.google.com/sql/docs/sqlserver/self-service-maintenance). See the [maintenance changelog](https://docs.cloud.google.com/sql/docs/sqlserver/maintenance-changelog) to learn more about these new maintenance versions.

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

## April 11, 2022

Feature

Cloud SQL for SQL Server supports in-place upgrades in Preview. You can upgrade your instance's major version or edition. For more information, see [Upgrade the database major version in-place](https://docs.cloud.google.com/sql/docs/sqlserver/upgrade-major-db-version-inplace).

## February 23, 2022

Feature

If your primary instance uses a private IP address, you can now select an allocated IP range for [clones](https://docs.cloud.google.com/sql/docs/sqlserver/clone-instance#cloning-an-instance-with-a-private-ip) and [replicas](https://docs.cloud.google.com/sql/docs/sqlserver/replication/create-replica#gcloud) created from the instance.

## February 17, 2022

Feature

Cloud SQL now supports the use of tags on instances. Tags are key-value pairs you can apply to your resources, such as a project or a Cloud SQL instance, which are used for fine-grained access control. To learn more, see [Access control with Google Cloud tags](https://docs.cloud.google.com/sql/docs/mysql/tags). To use tags now, see [Attach and manage tags on Cloud SQL instances](https://docs.cloud.google.com/sql/docs/mysql/manage-tags).

## February 08, 2022

Feature

Cross-region replication is now generally available in Cloud SQL for SQL Server.

You can use replication to scale the use of data in a database without degrading performance. Other reasons include migrating or maintaining data duplicates between regions.

For more information, see [Replication in Cloud SQL](https://docs.cloud.google.com/sql/docs/sqlserver/replication).

## February 07, 2022

Feature

SQL Server 2019 is now the default version. See [Database versions and version policies](https://docs.cloud.google.com/sql/docs/sqlserver/db-versions).

## January 31, 2022

Feature

The Key Access Justifications (KAJ) feature is now generally available in Cloud SQL. You can use KAJ as part of [Cloud External Key Manager (EKM)](https://docs.cloud.google.com/kms/docs/ekm). KAJ enables you to view the reason for each Cloud EKM request. Additionally, based on the justification provided, you can automatically approve or deny a request. For related information, see the [Overview](https://docs.cloud.google.com/cloud-provider-access-management/key-access-justifications/docs/overview).

## December 16, 2021

Feature

You can now see the database minor version when viewing information about an instance. See [Database versions and version policies](https://docs.cloud.google.com/sql/docs/sqlserver/db-versions) for a list of the latest supported versions.

## December 13, 2021

Feature

A new feature enables more flexibility for integrating Cloud SQL for SQL Server with Managed Service for Microsoft Active Directory. You can integrate your SQL Server instance with a managed AD domain located in a [different project](https://docs.cloud.google.com/sql/docs/sqlserver/configure-ad#integrating-different-project).

## November 16, 2021

Feature

Support for [southamerica-west1](https://docs.cloud.google.com/sql/docs/mysql/locations#location-r) (Santiago) region.

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

## September 10, 2021

Feature

The Cloud SQL [out-of-disk recommender](https://docs.cloud.google.com/sql/docs/mysql/using-ood-recommender) is now generally available. This feature proactively generates recommendations that help you reduce the risk of downtime that might be caused by your instances running out of disk space.

## August 21, 2021

Feature

Cloud SQL now supports [IAM Conditions](https://docs.cloud.google.com/sql/docs/mysql/project-access-control#iam-conditions). 

You can use IAM Conditions to define and enforce conditional, attribute-based access control for Google Cloud resources, including Cloud SQL instances. See [Overview of IAM Conditions](https://docs.cloud.google.com/iam/docs/conditions-overview) for more information.

## August 09, 2021

Feature

The Cloud SQL Admin API v1 is now generally available. It is and will continue to be compatible with the v1beta4 version. There is no requirement to migrate from v1beta4 to the v1 Admin API.

## August 03, 2021

Feature

Support for [northamerica-northeast2-a,b,c](https://docs.cloud.google.com/sql/docs/mysql/locations#location-r) (Toronto) region.

## June 29, 2021

Feature

Support for [asia-south2](https://docs.cloud.google.com/sql/docs/mysql/locations#location-r) (Delhi) region.

## June 28, 2021

Feature

Integration of SQL Server with Managed Service for Microsoft Active Directory is [generally available](https://docs.cloud.google.com/sql/docs/sqlserver/ad). 

This provides capabilities for authentication, authorization, and more.

[Joining an instance to a managed Active Directory domain](https://docs.cloud.google.com/sql/docs/sqlserver/configure-ad) enables you to log in to your SQL Server instances using Windows Authentication. Additionally, you can integrate with your on-premises AD domains by [establishing a trust](https://docs.cloud.google.com/managed-microsoft-ad/docs/create-trust) with the Managed Service for Microsoft Active Directory.

## June 24, 2021

Feature

Cloud SQL for SQL Server now supports SQL Server 2019. The default version continues to be SQL Server 2017 Standard. See [Database versions and version policies](https://docs.cloud.google.com/sql/docs/sqlserver/db-versions).

## June 23, 2021

Feature

Cloud SQL storage limits are now increased to support up to 64 TB. See [Cloud SQL storage limits](https://docs.cloud.google.com/sql/docs/quotas#storage_limits) for more information.

## June 21, 2021

Feature

A preview enables you to use replication in Cloud SQL for SQL Server. Additionally, the preview enables you to make cross-region replicas.

You can use replication to scale the use of data in a database without degrading performance. Other reasons include migrating or maintaining data duplicates between regions.

For more information, see [Replication in Cloud SQL](https://docs.cloud.google.com/sql/docs/sqlserver/replication).

Feature

Support for [australia-southeast2](https://docs.cloud.google.com/sql/docs/mysql/locations#location-r) (Melbourne) region.

## June 07, 2021

Feature

Cloud SQL now offers [faster maintenance](https://docs.cloud.google.com/sql/docs/sqlserver/maintenance#how_long_does_maintenance_take), with connectivity dropping for less than 120 seconds on average.

## May 19, 2021

Feature

Cloud SQL supports the preview version of the [out-of-disk recommender](https://docs.cloud.google.com/sql/docs/mysql/using-ood-recommender). This feature proactively generates recommendations that help you reduce the risk of downtime that might be caused by your instances running out of disk space. These recommendations can be applied when a Cloud SQL instance is trending towards the storage limit.

## April 30, 2021

Feature

The following version upgrade applies to Cloud SQL for SQL Server:

  * SQL Server 2017 is upgraded from 14.0.3257.3 to 14.0.3370.1



If you use maintenance windows, the new version will be available after your maintenance update. For information about maintenance windows, and to manage maintenance updates, see [Finding and setting maintenance windows](https://docs.cloud.google.com/sql/docs/sqlserver/set-maintenance-window).

## April 06, 2021

Feature

Cloud SQL for SQL Server enables you to perform change data capture (CDC) operations for your Cloud SQL instances. General information about CDC in SQL Server is [here](https://docs.microsoft.com/en-us/sql/relational-databases/track-changes/about-change-data-capture-sql-server?view=sql-server-ver15).

CDC is available for the following Cloud SQL for SQL Server database versions:

  * SQL Server 2017 Standard
  * SQL Server 2017 Enterprise



After [connecting](https://docs.cloud.google.com/sql/docs/sqlserver/connect-overview) to an instance, the `sqlserver` [user](https://docs.cloud.google.com/sql/docs/sqlserver/users) can do many [CDC operations](https://docs.microsoft.com/en-us/sql/relational-databases/track-changes/enable-and-disable-change-data-capture-sql-server?view=sql-server-ver15). The functions include (and are not limited to) the following: 

  * [cdc.fn_cdc_get_all_changes_<capture_instance>](https://docs.microsoft.com/en-us/sql/relational-databases/system-functions/cdc-fn-cdc-get-all-changes-capture-instance-transact-sql?view=sql-server-ver15)
  * [Sys.fn_cdc_get_max_lsn](https://docs.microsoft.com/en-us/sql/relational-databases/system-functions/sys-fn-cdc-get-max-lsn-transact-sql?view=sql-server-ver15)



To turn on this feature for a database, run this command:
    
    
    exec msdb.[dbo].[gcloudsql_cdc_enable_db] 'demo'
    

To turn off this feature for a database, run this command: `exec msdb.[dbo].[gcloudsql_cdc_disable_db] 'demo'`

Feature

Cloud SQL for SQL Server enables you to perform common operations on a [tempdb database](https://docs.microsoft.com/en-us/sql/relational-databases/databases/tempdb-database?view=sql-server-ver15). 

After you [connect](https://docs.cloud.google.com/sql/docs/sqlserver/connect-overview) to an instance, the `sqlserver` [user](https://docs.cloud.google.com/sql/docs/sqlserver/users) can manage the tempdb files. Specifically, the user has the `CONTROL` permission on the tempdb database, and can do many operations, including (and not limited to) the following: 
    
    
        *   ALTER DATABASE [tempdb] ADD FILE
        *   ALTER DATABASE [tempdb] REMOVE
    

## March 29, 2021

Feature

You can integrate Cloud SQL for SQL Server with Managed Service for Microsoft Active Directory. 

Authentication, authorization, and more [are available](https://docs.cloud.google.com/sql/docs/sqlserver/ad). For example, [joining an instance to a managed Active Directory domain](https://docs.cloud.google.com/sql/docs/sqlserver/configure-ad) enables you to log in using Windows Authentication. Additionally, you can integrate with your on-premises AD domains by [establishing a trust](https://docs.cloud.google.com/managed-microsoft-ad/docs/create-trust).

## March 24, 2021

Feature

Support for [europe-central2 (Warsaw )](https://docs.cloud.google.com/sql/docs/postgres/locations#location-r).

## February 10, 2021

Feature

The Cloud SQL Admin API v1beta4 is now generally available. The URL for the Admin API will continue to refer to v1beta4 for backward compatibility. To start using the Cloud SQL Admin API now, see [Using the Cloud SQL Admin API](https://docs.cloud.google.com/sql/docs/postgres/admin-api).

## January 13, 2021

Feature

Cloud SQL now exposes the metric `database/memory/total_usage`. This metric provides visibility into the database working set (including buffer cache). You can find this metric in the [Metrics explorer](https://docs.cloud.google.com/monitoring/charts/metrics-explorer) within the Monitoring dashboard. 

For more information about `database/memory/total_usage`, see [Cloud SQL Metrics](https://docs.cloud.google.com/monitoring/api/metrics_gcp#gcp-cloudsql).

## November 19, 2020

Feature

Cloud SQL for SQL Server now supports [retention settings for automated backups](https://docs.cloud.google.com/sql/docs/sqlserver/backup-recovery/backups#retention). You can configure retention of your automated backups for shorter or longer periods (1 to 365 days). The default setting remains 7 days.

## October 12, 2020

Feature

Cloud SQL now offers "deny maintenance periods". With [deny maintenance periods](https://docs.cloud.google.com/sql/docs/sqlserver/maintenance#deny), you can prevent automatic maintenance from occurring during a specific time period. For example, the end-of-year holiday season is a time of peak load that requires heightened focus on infrastructure stability for many retail businesses. By setting a deny maintenance period from mid-October to mid-January, these businesses can prevent planned upgrades from Cloud SQL during their busiest time of year.

## September 21, 2020

Feature

Cloud SQL for SQL Server enables you to [set a default collation value for databases in an instance](https://docs.cloud.google.com/sql/docs/sqlserver/instance-settings#collation). This collation value is a default for sorting rules, case, and accent sensitivity. You can set this value through the Cloud Console, the `gcloud` command, and the Cloud SQL Admin API.

## August 31, 2020

Feature

Cloud SQL for SQL Server supports [cloning](https://docs.cloud.google.com/sql/docs/sqlserver/clone-instance) using the Cloud Console, the `gcloud` command, and the Cloud SQL Admin API. When you clone an instance, you create an independent copy of the source instance.

## June 23, 2020

Feature

Committed use discounts (CUDs) are now available to purchase for Cloud SQL. CUDs provide discounted prices in exchange for your commitment to use a minimum level of resources for a specified term. With committed use discounts for Cloud SQL, you can earn a deep discount off your cost of use in exchange for committing to continuously use database instances in a particular region for a 1- or 3-year term. See the [documentation](https://docs.cloud.google.com/sql/docs/mysql/cud) for more details.

## June 08, 2020

Feature

Support for [asia-southeast2](https://docs.cloud.google.com/sql/docs/mysql/locations) region (Jakarta).

## April 20, 2020

Feature

Support for [us-west4](https://docs.cloud.google.com/sql/docs/sqlserver/locations) region (Las Vegas).

## March 24, 2020

Feature

Cloud SQL now supports 96-core machine types for MySQL, Postgres, and SQL Server instances. For pricing-related information, see the [Pricing page](https://cloud.google.com/sql/pricing).

## March 16, 2020

Feature

Cloud SQL instances using [private IP](https://docs.cloud.google.com/sql/docs/sqlserver/private-ip) are now accessible across regions, at the regular cross-region network egress cost.

## February 24, 2020

Feature

Support for us-west3 region (Salt Lake City).

## February 19, 2020

Feature

Cloud SQL for SQL Server now is generally available. Additionally, Cloud SQL for SQL Server includes new security and performance enhancements. To create SQL Server instances, see [Creating Instances](https://docs.cloud.google.com/sql/docs/sqlserver/create-instance).

## January 24, 2020

Feature

Support for [asia-northeast3](https://docs.cloud.google.com/sql/docs/sqlserver/locations) region (Seoul).

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

Cloud SQL now supports customer-managed encryption keys (CMEK). With CMEK, you can encrypt Cloud SQL instances using a key you manage. To learn more about CMEK, see the [Overview of customer managed encryption keys (CMEK)](https://docs.cloud.google.com/sql/docs/sqlserver/cmek). To start using CMEK, see [Using customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/sql/docs/sqlserver/configure-cmek).

## October 15, 2019

Feature

The beta version of Cloud SQL for SQL Server is available. To begin creating SQL Server instances, see [Creating Instances](https://docs.cloud.google.com/sql/docs/sqlserver/create-instance).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
