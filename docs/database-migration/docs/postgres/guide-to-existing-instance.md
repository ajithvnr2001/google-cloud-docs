---
url: https://docs.cloud.google.com/database-migration/docs/postgres/guide-to-existing-instance/
title: Migrate to an existing destination instance \u00a0|\u00a0 Database Migration Service for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T19:30:22.680011+00:00
---

# Migrate to an existing destination instance  |  Database Migration Service for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-migration/docs/postgres/guide-to-existing-instance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Database Migration Service ](https://docs.cloud.google.com/database-migration/docs)
  * [ PostgreSQL ](https://docs.cloud.google.com/database-migration/docs/postgres)
  * [ Guides ](https://docs.cloud.google.com/database-migration/docs/postgres/scenario-overview)



Send feedback 

#  Migrate to an existing destination instance Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to migrate your databases to a pre-existing Cloud SQL for PostgreSQL instance created directly in Cloud SQL.

This path is useful for scenarios where your destination instance is managed by a different team, or if you need to create the instance outside Database Migration Service (for example, if you use Terraform, need specific custom flags, or require advanced network topologies). If your migration has different requirements, consider following a different migration flow. For more information, see [ Get started with PostgreSQL migrations](https://docs.cloud.google.com/database-migration/docs/postgres/get-started-with-postgres-migrations).

At a high level, the migration follows these steps:

  1. Configure the source database to allow Database Migration Service to move your data to the new databases.
  2. Set up the network connectivity to your source PostgreSQL instance.
  3. Prepare and configure your existing destination Cloud SQL instance.
  4. Create the source connection profile and the migration job.
  5. Start and monitor the migration job.
  6. Promote the migration job and move your application to use the new databases.



## Costs

In this document, you use the following billable components of Google Cloud: 

  * Cloud SQL (See [ Cloud SQL pricing](https://docs.cloud.google.com/sql/pricing).)
  * If used for storing Customer-managed Encryption Keys (CMEK): Cloud Storage (See [ Cloud Storage pricing](https://docs.cloud.google.com/storage/pricing).) 



To generate a cost estimate based on your projected usage, use the [pricing calculator](https://docs.cloud.google.com/products/calculator). 

## Before you begin

  1. Verify if this migration path can fully support your scenario. See the following pages: 
     * [ Supported sources and destinations](https://docs.cloud.google.com/database-migration/docs/postgres/scenario-overview#supported-src-and-dest) on the _Scenario overview_ page lists all supported source and destination versions. 
     * [Known limitations for existing instances](https://docs.cloud.google.com/database-migration/docs/postgres/known-limitations#existing-instance-limitations) describes limitations, including the requirement that your existing destination instance must not contain existing user-defined data. 
  2. Consider in which region you want to create the destination database. Database Migration Service is a fully-regional product, meaning all entities related to your migration (source and destination connection profiles, migration jobs, destination databases, conversion workspaces) must be saved in a single region. 
  3. In the Google Cloud console, on the project selector page, select or [ create a Google Cloud project](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects). 

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  4. Enable the Database Migration Service and Cloud SQL Admin APIs. 

[ Enable the APIs](https://console.cloud.google.com//flows/enableapi?apiid=datamigration.googleapis.com,sqladmin.googleapis.com)




### Required roles

To get the permissions that you need to perform homogeneous PostgreSQL migrations with Database Migration Service, ask your administrator to grant you the required IAM roles on your project:

  * [ Database Migration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datamigration#datamigration.admin) (`roles/datamigration.admin`) 
  * [ Cloud SQL Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudsql#cloudsql.editor) (`roles/cloudsql.editor`) 
  * If you need to create or configure the destination instance outside Database Migration Service, you also need [ Cloud SQL Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudsql#cloudsql.admin) (`roles/cloudsql.admin`) 
  * [ Cloud SQL Studio User](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudsql#cloudsql.studioUser) (`roles/cloudsql.studioUser`) 



For more information about granting roles, see [ Manage access](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access) in the Identity and Access Management documentation. 

These predefined roles contain the permissions required to perform homogeneous PostgreSQL migrations with Database Migration Service. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to perform homogeneous PostgreSQL migrations with Database Migration Service: 

  * `datamigration.*`
  * `cloudsql.instances.create`
  * `cloudsql.instances.get`
  * `cloudsql.instances.list`
  * `cloudsql.instances.update`
  * `cloudsql.instances.delete`
  * `cloudsql.operations.get`
  * `cloudsql.users.list`
  * `cloudsql.users.get`
  * `cloudsql.users.create`
  * `cloudsql.users.update`
  * `cloudsql.users.delete`



You might also be able to get these permissions with [ custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [ predefined roles](https://docs.cloud.google.com/iam/docs/roles-permissions). 

## Prepare your source database

To prepare your source data for migration, follow these steps:

  1. [ Choose and configure your source network connectivity method](https://docs.cloud.google.com/database-migration/docs/postgres/networking-methods). 
  2. Configure your source database instance. At a high level, this includes the following steps: 
     1. Install the `pglogical` PostgreSQL extension (version 2.2.1 or later) on the source database and on all databases to be migrated.
     2. Configure PostgreSQL parameters: set `wal_level = logical`, and ensure adequate values for `max_replication_slots`, `max_wal_senders`, and `max_worker_processes`.
     3. Grant replication privileges to your migration user, and configure `pg_hba.conf` to permit connections from the destination Cloud SQL instance. 

For detailed instructions, see [ Configure your source database](https://docs.cloud.google.com/database-migration/docs/postgres/configure-source-database). 

  3. [ Create the source connection profile](https://docs.cloud.google.com/database-migration/docs/postgres/create-connection-profiles). 



## Prepare and configure your destination instance

When migrating to an existing Cloud SQL instance (such as an instance pre-provisioned by another team or managed with Terraform), ensure that the instance satisfies all Database Migration Service prerequisites before creating your migration job:

  1. **Instance readiness and data state** : 
     * The destination instance must be a standalone instance (not a replica) in the `RUNNABLE` state. 
     * The instance must reside in the same Google Cloud region as your migration job and connection profile. 
     * The instance can only be associated with one active migration job at a time. 
     * The destination instance must not contain existing user data, user-defined tables, or non-system databases. The migration job verification fails if existing user data is present on the instance. For more information, see [ Limitations for migrations to existing destination instances](https://docs.cloud.google.com/database-migration/docs/postgres/known-limitations#existing-instance-limitations). If necessary, [ clear existing data from your destination instance](https://docs.cloud.google.com/database-migration/docs/postgres/diagnose-issues#clear-ext-instance-data-steps). 
  2. **Database flag configuration** : Enable the `cloudsql.enable_pglogical` flag on your destination Cloud SQL for PostgreSQL instance. This flag is required for logical replication. For more information on setting flags, see [ Configuring database flags](https://docs.cloud.google.com/sql/docs/postgres/flags). 
  3. **Database user credentials and permissions** : Ensure that the required administrative database user accounts exist on your destination instance (such as the default `postgres` user or a dedicated migration user with the `cloudsqlsuperuser` role) to manage databases and roles. You can create and manage database users using standard `psql` commands or through the Google Cloud console. For more information, see [ Manage users](https://docs.cloud.google.com/sql/docs/postgres/create-manage-users) in the Cloud SQL documentation. 
  4. **Network connectivity requirements** : Verify that your destination instance's networking is properly configured to communicate with your source database according to your chosen connectivity method: 
     * **Private Service Connect** : If your destination instance is Private Service Connect-enabled, it must have a Private Service Connect Outbound Network Attachment configured. See [ Private Service Connect outbound connections](https://docs.cloud.google.com/sql/docs/postgres/about-private-service-connect#psc-outbound) in the Cloud SQL documentation. 
     * **Virtual Private Cloud peering (Private Services Access / Private IP)** : The destination instance must have private IP enabled on the Virtual Private Cloud network that peers with or routes to your source database. See [ Configure private IP](https://docs.cloud.google.com/sql/docs/postgres/configure-private-ip). 
     * **Public IP allowlist** : If using public IP connectivity, ensure that you enable public IP on your destination instance and you allowlist the instance outgoing IP addresses (including both primary and secondary outgoing IPs if the instance is configured for high availability) in your source firewall. See [ Authorize networks for public IP](https://docs.cloud.google.com/sql/docs/postgres/authorize-networks). 
  5. **Instance demotion notice** : 
     * For standard PostgreSQL migrations, Database Migration Service demotes the existing standalone destination instance to configure it as an external replica of your source database. You must confirm this demotion when creating the migration job in the Google Cloud console by entering the destination instance ID. 
     * Demoting the instance doesn't place the Cloud SQL for PostgreSQL database into read-only mode, but you must avoid write operations on tables or databases participating in the migration to prevent replication conflicts. 
     * Automated backups, point-in-time recovery (PITR), and creating Cloud SQL read replicas are suspended until you promote the migration job. For more information, see [ Limitations for migrations to existing destination instances](https://docs.cloud.google.com/database-migration/docs/postgres/known-limitations#existing-instance-limitations). 
     * If you manage your destination instance using infrastructure-as-code (such as Terraform), Database Migration Service modifies backup and recovery settings during migration. For guidance on handling Terraform configuration drift, see [ Diagnose issues](https://docs.cloud.google.com/database-migration/docs/postgres/diagnose-issues#existing-instance-terraform-config-drift). 



## Create and run the migration job

To configure and run your migration, perform the following steps:

  1. Optional: If you want to manage your own certificates or encryption keys for the migration job, [ prepare the necessary encryption keys](https://docs.cloud.google.com/sql/docs/postgres/configure-cmek). 
  2. [ Create and run the migration job for an existing destination instance](https://docs.cloud.google.com/database-migration/docs/postgres/create-migration-job-existing-instance). 

You can monitor the migration progress, as well as your destination instance health with Database Migration Service observability features. See [ Migration job metrics](https://docs.cloud.google.com/database-migration/docs/postgres/migration-job-metrics). 




## Finalize the migration

When you decide to switch your application to the new Cloud SQL for PostgreSQL instance, finalize the migration by following these steps:

  1. _Optional_ : [ Set up cascading read replicas](https://docs.cloud.google.com/database-migration/docs/postgres/set-up-cascading-replica). If you want to use cascading read replicas, you can configure them when the migration job enters the CDC phase. 
  2. Stop all write operations on your source database. You can switch them to read-only mode to retain operational functionality.
  3. [ Promote the migration job](https://docs.cloud.google.com/database-migration/docs/postgres/promote-migration).
  4. Optional: [ Verify migration data](https://docs.cloud.google.com/database-migration/docs/postgres/verify-migration) for completeness.
  5. If you manage your destination database using infrastructure-as-code (such as Terraform), re-apply your configuration after promotion to reconcile any settings adjusted by Database Migration Service during migration. 



## What's next

Learn more about Google Cloud features for Cloud SQL for PostgreSQL. See [ Cloud SQL for PostgreSQL features](https://docs.cloud.google.com/sql/docs/postgres/features).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-19 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-19 UTC."],[],[]] 
