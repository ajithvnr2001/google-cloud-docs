---
url: https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/faq/
title: Database Migration Service for AlloyDB FAQ \u00a0|\u00a0 Database Migration Service for PostgreSQL to AlloyDB \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T21:41:30.617507+00:00
---

# Database Migration Service for AlloyDB FAQ  |  Database Migration Service for PostgreSQL to AlloyDB  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/faq/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Database Migration Service ](https://docs.cloud.google.com/database-migration/docs)
  * [ PostgreSQL to AlloyDB ](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb)
  * [ Resources ](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/resources)



Send feedback 

#  Database Migration Service for AlloyDB FAQ Stay organized with collections  Save and categorize content based on your preferences. 

[MySQL](https://docs.cloud.google.com/database-migration/docs/mysql/faq "View this page for the MySQL version of Database Migration Service.") | [PostgreSQL](https://docs.cloud.google.com/database-migration/docs/postgres/faq "View this page for the PostgreSQL version of Database Migration Service.") | PostgreSQL to AlloyDB

  
  


  * What is Database Migration Service?
  * Which sources are supported?
  * Is there cross-version support?
  * Which data, schema, and metadata components are migrated?
  * Which changes are replicated during continuous migration?
  * What isn't migrated?
  * Which networking methods are used?
  * What are the known limitations?



What is Database Migration Service?
    Database Migration Service is a service that makes it easier for you to migrate your data to Google Cloud. Database Migration Service helps you lift and shift your PostgreSQL workloads into AlloyDB.
Which sources are supported?
    

  * Amazon RDS 9.6.10+, 10.5+, 11.1+, 12, 13, 14, 15, 16, 17
  * Amazon Aurora 10.11+, 11.6+, 12.4+, 13.3+, 14, 15, 16, 17
  * Self-managed PostgreSQL (on premises or on any cloud VM that you fully control) 9.4, 9.5, 9.6, 10, 11, 12, 13, 14, 15, 16, 17
  * Cloud SQL 9.6, 10, 11, 12, 13, 14, 15, 16, 17


Which destinations are supported?
    

  * AlloyDB for PostgreSQL 14, 15, 16, 17, 18


Is there cross-version support?
     Database Migration Service supports PostgreSQL to AlloyDB migrations from any of the supported source database versions. 
Which data, schema, and metadata components are migrated?
    Database Migration Service migrates schema, data, and metadata from the source to the destination. All of the following data, schema, and metadata components are migrated as part of the database migration: 

Data Migration 

  * All schemas and all tables from the selected database.

Schema Migration
  * Naming
  * Primary key
  * Data type
  * Ordinal position
  * Default value
  * Nullability
  * Auto-increment attributes
  * Secondary indexes

Metadata Migration 
  * Stored Procedures
  * Functions
  * Triggers
  * Views
  * Foreign key constraints


Which changes are replicated during continuous migration?
     Only DML changes are automatically updated during the migration. Managing DDL so that the source and destination database(s) remain compatible is the responsibility of the user, and can be achieved in two ways: 

  1. Stop writes to the source and run the DDL commands in both the source and the destination. Before running DDL commands on the destination, grant the `alloydbexternalsync` role to the Cloud SQL user applying the DDL changes. To enable querying or changing the data, grant the `alloydbexternalsync` role to the relevant Cloud SQL users.
  2. Use the `pglogical.replicate_ddl_command` to run DDL on the source and destination at a consistent point. The user running this command must have the same username on both the source and the destination, and should be the superuser or the owner of the artifact being migrated (for example, the table, sequence, view, or database).

Here are a few examples of using the `pglogical.replicate_ddl_command`.

To add a column to a database table, run the following command:

`select pglogical.replicate_ddl_command('ALTER TABLE [schema].[table] add column surname varchar(20)', '{default}');`

To change the name of a database table, run the following command:

`select pglogical.replicate_ddl_command('ALTER TABLE [schema].[table] RENAME TO [table_name]','{default}');`

To create a database table, run the following commands:

     1. `select pglogical.replicate_ddl_command(command := 'CREATE TABLE [schema].[table] (id INTEGER PRIMARY KEY, name VARCHAR);', replication_sets := ARRAY['default'']);`
     2. `select pglogical.replication_set_add_table('default', '[schema].[table]');`


What isn't migrated?
    

To add users to the AlloyDB destination instance, add them from the PostgreSQL client. Learn more about [creating and managing PostgreSQL users](https://cloud.google.com/sql/docs/postgres/create-manage-users).

[Large objects](https://www.postgresql.org/docs/current/largeobjects.html) can't be replicated because PostgreSQL's logical decoding facility doesn't support decoding changes to large objects. For tables that have [ column type oid](https://www.postgresql.org/docs/current/datatype-oid.html) referencing large objects, the rows are still synced, and new rows are replicated. However, trying to access the large object on the destination database (read using [lo_get](https://www.postgresql.org/docs/current/lo-funcs.html), export using [lo_export](https://www.postgresql.org/docs/current/lo-funcs.html), or check the catalog `pg_largeobject` for the given oid), fails with a message saying that the large object doesn't exist.

For tables that don't have primary keys, Database Migration Service supports migration of the **initial snapshot and`INSERT` statements during the change data capture (CDC) phase**. You should migrate `UPDATE` and `DELETE` statements manually.

Database Migration Service doesn't migrate data from materialized views, just the view schema. To populate the views, run the following command: `REFRESH MATERIALIZED VIEW view_name`.

The `SEQUENCE` states (for example, `last_value`) on the new AlloyDB destination might vary from the source `SEQUENCE` states.

Which networking methods are used?
    To create a migration in Database Migration Service, connectivity must be established between the source and the Cloud SQL destination instance. There are a variety of methods supported. Choose the one that works best for the specific workload.   
Networking method | Description | Pros | Cons  
---|---|---|---  
Reverse SSH tunnel through cloud-hosted VM | Establishes connectivity from the destination to the source through a secure reverse SSH tunnel. Requires a bastion host VM in the Google Cloud project and a machine (for example, a laptop on the network) that has connectivity to the source. Database Migration Service collects the required information at migration creation time, and auto-generates the script for setting it up. | 

  * Easy to configure.
  * Doesn't require any custom firewall configuration.
  * Recommended for short-lived migration scenarios (POC or small database migrations).

| 

  * You own and manage the Bastion VM.
  * May incur additional costs.

  
TCP Proxy via a cloud-hosted VM | Establishes connectivity from the destination to the source through a TCP proxy via Cloud hosted VM. Database Migration Service collects the required information at migration creation time, and auto-generates the script for setting it up. Relevant on AlloyDB migrations where the source is on the old network architecture.  | 

  * Easy to configure.
  * Doesn't require any custom firewall configuration.

| 

  * The Bastion VM is owned and managed by you, and may incur additional costs.

  
VPC peering | This method works by configuring the VPCs to communicate with one another. | 

  * Native Google Cloud solution.
  * Easy to configure.
  * High-bandwidth
  * Recommended for long-running or high-volume migrations.

| Only applicable if both the source and destination databases are hosted in Google Cloud.  
VPN | Sets up an IPSec VPN tunnel connecting the internal network and Google Cloud VPC through a secure connection over the public Internet. Use Google Cloud VPN or any VPN solution that is set up for the internal network. | 

  * Robust and scalable connectivity solution.
  * Medium-high bandwidth.
  * Security built-in.
  * Offered as Google Cloud solutions or from other 3rd parties.

| 

  * Additional cost.
  * Non-trivial configuration (unless already in-place).

  
Cloud Interconnect | Uses a highly available, low latency connection between the on-premises network and Google Cloud. | Highest bandwidth, ideal for long-running high-volume migrations. | 

  * Additional cost.
  * Connection isn't secure by default.
  * Non-trivial configuration (unless already in-place).

  
What are the known limitations?
     See [Known limitations](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/known-limitations).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 

  * ### Products and pricing

    * [ See all products ](https://cloud.google.com/products/)
    * [ Google Cloud pricing ](https://cloud.google.com/pricing/)
    * [ Google Cloud Marketplace ](https://cloud.google.com/marketplace/)
    * [ Contact sales ](https://cloud.google.com/contact/)
  * ### Support

    * [ Community forums ](https://discuss.google.dev/c/google-cloud/14/)
    * [ Support ](https://cloud.google.com/support-hub/)
    * [ Release Notes ](https://docs.cloud.google.com/release-notes)
    * [ System status ](https://status.cloud.google.com)
  * ### Resources

    * [ GitHub ](https://github.com/googlecloudPlatform/)
    * [ Getting Started with Google Cloud ](https://docs.cloud.google.com/docs/get-started/)
    * [ Code samples ](https://docs.cloud.google.com/docs/samples)
    * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture/)
    * [ Training and Certification ](https://cloud.google.com/learn/training/)
  * ### Engage

    * [ Blog ](https://cloud.google.com/blog/)
    * [ Events ](https://cloud.google.com/events/)
    * [ X (Twitter) ](https://x.com/googlecloud)
    * [ Google Cloud on YouTube ](https://www.youtube.com/googlecloud)
    * [ Google Cloud Tech on YouTube ](https://www.youtube.com/googlecloudplatform)



[ ![Google Developers](https://www.gstatic.com/devrel-devsite/prod/v097103d8ccd7b257790809ea4cc5e5fee6daa6e24890a4af388296e58364bc31/clouddocs/images/lockup-google-for-developers.svg)](https://developers.google.com/)

  * [ Android ](https://developer.android.com/)
  * [ Chrome ](https://developer.chrome.com/)
  * [ Firebase ](https://firebase.google.com/)
  * [ Google AI ](https://ai.google.com/)



  * [ About Google ](https://about.google/)
  * [ Privacy ](https://policies.google.com/privacy)
  * [ Site terms ](https://policies.google.com/terms?hl=en)
  * [ Google Cloud terms ](https://cloud.google.com/product-terms)
  * Manage cookies 
  * [ Our third decade of climate action: join us ](https://cloud.google.com/sustainability)
  * Sign up for the Google Cloud newsletter [ Subscribe ](https://cloud.google.com/newsletter/)



  * English
  * Deutsch
  * Español
  * Español – América Latina
  * Français
  * Indonesia
  * Italiano
  * Português
  * Português – Brasil
  * עברית
  * 中文 – 简体
  * 中文 – 繁體
  * 日本語
  * 한국어


