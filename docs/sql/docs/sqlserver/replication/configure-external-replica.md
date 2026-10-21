---
url: https://docs.cloud.google.com/sql/docs/sqlserver/replication/configure-external-replica/
title: Configure external replicas \u00a0|\u00a0 Cloud SQL for SQL Server \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:31:23.518580+00:00
---

# Configure external replicas  |  Cloud SQL for SQL Server  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/sqlserver/replication/configure-external-replica/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ SQL Server ](https://docs.cloud.google.com/sql/docs/sqlserver)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/sqlserver/features)



Send feedback 

#  Configure external replicas Stay organized with collections  Save and categorize content based on your preferences. 

[MySQL](https://docs.cloud.google.com/sql/docs/mysql/replication/configure-external-replica "View this page for the MySQL database engine") | [PostgreSQL](https://docs.cloud.google.com/sql/docs/postgres/replication/configure-external-replica "View this page for the PostgreSQL database engine") | SQL Server

This page describes how to set up a Cloud SQL instance to publish to a subscriber that is external to Cloud SQL or that is within Cloud SQL. External replication in Cloud SQL for SQL Server uses transactional replication, in which Cloud SQL acts as a publisher to a subscriber.

Transactional replication supports publishing several types of objects, as [documented](https://docs.microsoft.com/en-us/sql/relational-databases/replication/publish/publish-data-and-database-objects?view=sql-server-ver15) by Microsoft. Additionally, in Cloud SQL, limitations on this feature are similar to those [documented](https://docs.microsoft.com/en-us/sql/relational-databases/replication/publish/publish-data-and-database-objects?view=sql-server-ver15#limitations-on-publishing-objects) by Microsoft.

Some of the supported objects are the following:

  * Tables
  * Stored Procedures
  * Views
  * Index views
  * User Defined Functions



Although examples of the publication process are on this page, see [Publish Data and Database Objects](https://docs.microsoft.com/en-us/sql/relational-databases/replication/publish/publish-data-and-database-objects?view=sql-server-ver15) in the Microsoft documentation for details. Consider using [SQL Server Management Studio (SSMS)](https://docs.microsoft.com/en-us/sql/ssms/download-sql-server-management-studio-ssms?view=sql-server-ver15) in your publication process, as your available options may be more apparent in SSMS.

Also see [About replication in Cloud SQL](https://docs.cloud.google.com/sql/docs/sqlserver/replication).

**Note:** For reference information about the stored procedures provided in the examples on this page, see [Cloud SQL stored procedures](https://docs.cloud.google.com/sql/docs/sqlserver/stored-procedures).

## Implementing transactional replication

A Cloud SQL instance can act as a publisher and distributor for an external subscriber, through transactional replication.

To set up transactional replication, you can:

  * Use stored procedures provided by Cloud SQL. These are prefixed by: `gcloudsql_transrepl_`
  * Refine replication using stored procedures provided by Microsoft



### Limitations and prerequisites

As you plan for transactional replication, review this section.

#### Limitations

  * Instances that use high availability (HA) lack a consistent, outgoing IP address. Such instances cannot be publishers if they utilize public IP connectivity. Thus, if an instance uses HA, it must use Private IP connectivity. 
  * If you use Private Service Connect, ensure that [outbound connectivity is set up](https://docs.cloud.google.com/sql/docs/sqlserver/configure-private-service-connect#configure-psc-outbound) on the publisher instance. 
  * For defining an article, see [Define an Article](https://docs.microsoft.com/en-us/sql/relational-databases/replication/publish/define-an-article?view=sql-server-ver15) in the Microsoft documentation, including for the limitations and restrictions. 
  * The stored procedures provided by Cloud SQL support push subscription only. 
  * External replication can't be configured on an instance configured with [replication](https://docs.cloud.google.com/sql/docs/sqlserver/replication/create-replica). 



#### Prerequisites

Bi-directional network connectivity must be set up between a Cloud SQL instance and the subscriber instance. The subscriber can be external as in, for example, an on-premises subscriber, or the subscriber can be internal to Cloud SQL.

For Cloud SQL instances that use public IPs, Cloud SQL uses a different IP address on its egress and ingress paths. The replica must allow-list the primary instance's outgoing IP address, which you can retrieve using the `gcloud` command:
    
    
    gcloud sql instances describe [PRIMARY_NAME] --format="default(ipAddresses)"
    

To use Cloud SQL private IP with an on-premises instance, you must set up private services access. This requires peering between the Cloud SQL VPC and customer's VPC over a custom IP range that needs to be advertised.

To use Cloud SQL with Private Service Connect, see [Configure Private Service Connect](https://docs.cloud.google.com/sql/docs/sqlserver/configure-private-service-connect). When using Private Service Connect, you must ensure that [outbound connectivity is set up](https://docs.cloud.google.com/sql/docs/sqlserver/configure-private-service-connect#configure-psc-outbound) on the publisher instance to allow communication with the subscriber.

When connecting from on-premises, the on-premises firewall must allow inbound and outbound connections. Specifically, the on-premises firewall must allow such connections on port 1433 to the private services access subnet range that's used for the specific Google Cloud service (in this case, for Cloud SQL). Consider allowing a subnet range rather than a specific IP for each instance created.

For related information, see the following:

  * [Configure private IP](https://docs.cloud.google.com/sql/docs/sqlserver/configure-private-ip) (which includes a link for setting up private services access)
  * [Configure Private Service Connect](https://docs.cloud.google.com/sql/docs/sqlserver/configure-private-service-connect)
  * [private services access](https://docs.cloud.google.com/vpc/docs/private-services-access)
  * [Configuring private services access](https://docs.cloud.google.com/vpc/docs/configure-private-services-access)



### Permissions and roles

The following sections cover permissions and roles.

#### Packaged permissions

The stored procedures provided by Cloud SQL include the permissions needed for transactional replication. These are wrapper stored procedures that sometimes call one or more Microsoft stored procedures. See the [Microsoft documentation](https://docs.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/replication-stored-procedures-transact-sql?view=sql-server-ver15) for information about the Microsoft stored procedures.

#### Required role

The accounts utilized (including for the log reader agent) need a `db_owner` role, as in the case of the `sqlserver` user. For necessary information, review the [Replication Agent Security Model](https://docs.microsoft.com/en-us/sql/relational-databases/replication/security/replication-agent-security-model?redirectedfrom=MSDN&view=sql-server-ver15).

### Using stored procedures for publishing, distributing, and subscribing

This section contains suggested steps for setting up transactional replication.

The `sqlserver` user has stored procedures to set up your Cloud SQL instance to act as a publisher. For reference information, see [Cloud SQL stored procedures](https://docs.cloud.google.com/sql/docs/sqlserver/stored-procedures).

#### Preparing for transactional replication with a test database

Before setting up transactional replication for a production database, you can set up your instance as a publisher of test database objects. On this page, the test database is called the `pub_demo` database.

Connect to your Cloud SQL instance using the `sqlserver` user and create a database for testing purposes. For example:
    
    
    Create Database pub_demo;
    GO
    USE pub_demo;
    CREATE TABLE Employee(employeeId INT primary key);
    INSERT INTO Employee([employeeId]) VALUES (1);
    INSERT INTO Employee([employeeId]) VALUES (2);
    
    -- Add procedure
    CREATE OR ALTER PROCEDURE dbo.p_GetDate
    AS
    SELECT getdate()
    
    -- Add view
    CREATE OR ALTER VIEW dbo.v_GetDbs
    AS
    SELECT name from sys.databases
    
    -- Function
    CREATE OR ALTER FUNCTION dbo.fn_ListDbFiles(@id int)
    RETURNS TABLE
    AS
    RETURN
    (
    select * from sys.master_files where database_id = @id
    )
    

#### Set up the distribution database

For the distribution database, you can use `msdb.dbo.gcloudsql_transrepl_setup_distribution`, which is a wrapper stored procedure for these Microsoft stored procedures:

  * [sp_adddistributor](https://docs.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/sp-adddistributor-transact-sql?view=sql-server-ver15)
  * [sp_adddistributiondb](https://docs.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/sp-adddistributiondb-transact-sql?view=sql-server-ver15)
  * [sp_adddistpublisher](https://docs.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/sp-adddistpublisher-transact-sql?view=sql-server-ver15)



For example:
    
    
    EXEC msdb.dbo.gcloudsql_transrepl_setup_distribution @login='sqlserver', @password='<password>'
    

#### Enable a database for publication

To enable or disable the publishing option of a database, you can use `msdb.dbo.gcloudsql_transrepl_replicationdboption`. This stored procedure applies to the publishing option for the publisher that uses [sp_replicationdboption](https://docs.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/sp-replicationdboption-transact-sql?view=sql-server-ver15).

For example:
    
    
    EXEC msdb.dbo.gcloudsql_transrepl_replicationdboption @db='pub_demo', @value='true'
    

#### Add a log reader agent

You can set up a log reader agent for a database that uses [sp_addlogreader_agent](https://docs.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/sp-addlogreader-agent-transact-sql?view=sql-server-ver15).

For example:
    
    
    EXEC msdb.dbo.gcloudsql_transrepl_addlogreader_agent @db='pub_demo', @login='sqlserver', @password='<password>'
    

#### Create the publication for the database

You can use `msdb.dbo.gcloudsql_transrepl_addpublication` to create a transactional publication for the database you specify. This stored procedure wraps [sp_addpublication](https://docs.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/sp-addpublication-transact-sql?view=sql-server-ver15).

For example:
    
    
    EXEC msdb.dbo.gcloudsql_transrepl_addpublication @db='pub_demo', @publication='pub1'
    

#### Create a snapshot agent for the specified publication

To create a snapshot agent for the publisher database, you can use `msdb.dbo.gcloudsql_transrepl_addpublication_snapshot`, which wraps [sp_addpublication_snapshot](https://docs.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/sp-addpublication-snapshot-transact-sql?view=sql-server-ver15).

For example:
    
    
    EXEC msdb.dbo.gcloudsql_transrepl_addpublication_snapshot @db='pub_demo',  @publication='pub1', @login='sqlserver', @password='<password>'
    

#### Create an article and add it to the publication

You can create an article from within the publisher database and add it to the publication. As the `sqlserver` user, utilize [sp_addarticle](https://docs.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/sp-addarticle-transact-sql?view=sql-server-ver15).

You also may add articles using SSMS. For more information, see [Add Articles to and Drop Articles from a Publication](https://docs.microsoft.com/en-us/sql/relational-databases/replication/publish/add-articles-to-and-drop-articles-from-a-publication?view=sql-server-ver15).

For example:
    
    
    USE pub_demo;
    GO
    
    EXEC sp_addarticle @publication = 'pub1',
                       @article = 'csql_dbo.employee',
                       @source_owner = 'dbo',
                       @source_object = 'Employee',
                       @description = N'cloudsql_article_table',
                       @schema_option = 0x000000000903409D,
                       @identityrangemanagementoption = N'manual',
                       @destination_table = 'Employee',
                       @destination_owner = 'dbo';
    
    -- add function
    use [pub_demo]
    exec sp_addarticle  @publication = N'pub1',
                       @article = N'fn_ListDbFiles',
                       @source_owner = N'dbo',
                       @source_object = N'fn_ListDbFiles',
                       @type = N'func schema only',
                       @description = N'',
                       @creation_script = N'',
                       @pre_creation_cmd = N'drop',
                       @schema_option = 0x0000000008000001,
                       @destination_table = N'fn_ListDbFiles',
                       @destination_owner = N'dbo',
                       @status = 16
    
    -- add procedure
    use [pub_demo]
    exec sp_addarticle  @publication = N'pub1',
                       @article = N'p_GetDate',
                       @source_owner = N'dbo',
                       @source_object = N'p_GetDate',
                       @type = N'proc schema only',
                       @description = N'',
                       @creation_script = N'',
                       @pre_creation_cmd = N'drop',
                       @schema_option = 0x0000000008000001,
                       @destination_table = N'p_GetDate',
                       @destination_owner = N'dbo',
                       @status = 16
    
    -- add view
    use [pub_demo]
    exec sp_addarticle  @publication = N'pub1',
                       @article = N'v_GetDbs',
                       @source_owner = N'dbo',
                       @source_object = N'v_GetDbs',
                       @type = N'view schema only',
                       @description = N'',
                       @creation_script = N'',
                       @pre_creation_cmd = N'drop',
                       @schema_option = 0x0000000008000001,
                       @destination_table = N'v_GetDbs',
                       @destination_owner = N'dbo',
                       @status = 16
    
    

#### Add the subscription to the publication

From within the database, you can add the subscription to the publication. As the `sqlserver` user, set the subscriber status by using [sp_addsubscription](https://docs.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/sp-addsubscription-transact-sql?view=sql-server-ver15).

For example:
    
    
    Use pub_demo;
    GO
    EXEC sp_addsubscription @publication ='pub1',
                            @subscriber = N'10.10.100.1,1433',
                            @destination_db = pub_demo,
                            @subscription_type = N'Push',
                            @sync_type = N'automatic',
                            @article = N'all',
                            @update_mode = N'read only',
                            @subscriber_type = 0
    
    

#### Connect to the subscriber and create a subscription database

You can connect to the subscriber and create a subscription database for replicated data to populate.

For example:
    
    
     Create Database pub_demo
    

#### Add a new scheduled agent job to synchronize the push subscription

You can add a new scheduled agent job to synchronize the push subscription to the publication. For example, on the publisher database, run a command similar to the one below. This command uses `msdb.dbo.gcloudsql_transrepl_addpushsubscription_agent`, a wrapper stored procedure for [sp_addpushsubscription_agent](https://docs.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/sp-addpushsubscription-agent-transact-sql?view=sql-server-ver15):
    
    
    EXEC msdb.dbo.gcloudsql_transrepl_addpushsubscription_agent
    @db='pub_demo',
    @publication = 'pub1',
    @subscriber_db= 'pub_demo',
    @subscriber_login='sqlserver',
    @subscriber_password='<password>',
    @subscriber='11.11.111.1,1433'
    
    

#### Start a publication snapshot agent job

You can start a publication snapshot agent job, as follows:
    
    
    USE pub_demo;
    EXEC sp_startpublication_snapshot
    @publication = 'pub1'
    

#### Grant access to an account to use the Replication Monitor

Use `msdb.dbo.gcloudsql_transrepl_addmonitoraccess` to:

  * Provide access to the Replication Monitor in SSMS
  * Query tables in the distribution database



Thus, this stored procedure lets you use the SELECT statement on the distribution database's replication-related tables, such as the [MSrepl_errors](https://docs.microsoft.com/en-us/sql/relational-databases/system-tables/msrepl-errors-transact-sql?view=sql-server-ver15) table:
    
    
    EXEC msdb.dbo.gcloudsql_transrepl_addmonitoraccess
    @login = 'sqlserver'
    
    

#### Change a distribution database property

You can change the `heartbeat_interval`. Use the `msdb.dbo.gcloudsql_transrepl_changedistributor_property` procedure, which wraps `sp_changedistributor_property`.

For more information, see the [documentation](https://docs.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/sp-changedistributor-property-transact-sql?view=sql-server-ver16) for `sp_changedistributor_property`. Also see that documentation for more information about the `heartbeat_interval` value.

For example:
    
    
    EXEC msdb.dbo.gcloudsql_transrepl_changedistributor_property
    @property = N'heartbeat_interval',
    @value = 90
    

#### Use the Replication Monitor

Right-click the replication node in SSMS and choose **Launch Replication Monitor**.

If you click the Agents tab, you should see a view similar to the following:

![Folders on Agents tab](https://docs.cloud.google.com/static/sql/images/publisher-agents-tab.png)

### Using stored procedures for removing replication

This section contains suggested steps for removing transactional replication.

#### Drop the subscription

To drop the subscription, use the `sp_dropsubscription` stored procedure.

Here is an example of the commands to drop the subscription:
    
    
    USE  pub_demo;
    GO
    EXEC sp_dropsubscription
              @publication = 'csql_pub_pub_demo',
              @article     = N'all',
              @subscriber  = N'11.11.111.1,1433'
    

**Note:** On the following versions of SQL Server, don't specify the port when you use commands similar to the example for dropping the subscription: SQL Server 2019 Standard, SQL Server 2019 Enterprise, SQL Server 2019 Express, SQL Server 2019 Web, SQL Server 2022 Standard, SQL Server 2022 Enterprise, SQL Server 2022 Express, and SQL Server 2022 Web.

#### Drop the subscriber

To drop the subscriber, use the `msdb.dbo.gcloudsql_transrepl_dropsubscriber` stored procedure:
    
    
    EXEC msdb.dbo.gcloudsql_transrepl_dropsubscriber
     @subscriber  = N'11.11.111.1,1433'
    

#### Drop the publication

To drop the publication, use the `msdb.dbo.gcloudsql_transrepl_droppublication` stored procedure:
    
    
    EXEC msdb.dbo.gcloudsql_transrepl_droppublication
      @db = 'pub_demo', @publication='pub1'
    

#### Disable the publication database

To disable the publication database, use the `msdb.dbo.gcloudsql_transrepl_replicationdboption` stored procedure:
    
    
    EXEC msdb.dbo.gcloudsql_transrepl_replicationdboption
    @db='pub_demo',
    @value=N'false'
    

#### Remove the distribution database

To remove the distribution database, use the `msdb.dbo.gcloudsql_transrepl_remove_distribution` stored procedure:
    
    
    EXEC msdb.dbo.gcloudsql_transrepl_remove_distribution
    

### Tips and steps for troubleshooting issues

The following sections cover common troubleshooting topics.

#### Running stored procedures from the right database

You may get the following error when running `sp_addarticle`, `sp_addsubscription`, or `sp_startpublication_snapshot`:
    
    
    Only members of the sysadmin fixed server role or db_owner fixed database role can perform this operation.
    

Additionally, you may get the following error when running `sp_dropsubscription`:
    
    
    This database is not enabled for publication.
    

If these errors occur, note that you must run those stored procedures from within the database for which they apply. You can use the following to confirm they are run from the correct database:
    
    
    USE <database_name>;
    GO
    <Run stored proc>
    

#### Replication

Replication errors are provided in SQL error logs and elsewhere. You can query some tables in the distribution database directly for replication errors. For example:
    
    
    select * from [cloudsql_distribution]..msrepl_errors
    select * from [cloudsql_distribution]..MSreplication_monitordata
    

Microsoft has more [examples](https://docs.microsoft.com/en-us/sql/relational-databases/replication/troubleshoot-tran-repl-errors?view=sql-server-ver15) about looking up errors using the Replication Monitor. For example, the `sqlserver` user may lack access to a command.

#### Replication agent jobs

After replication is set up, the new SQL agent jobs aren't visible in SSMS to the `sqlserver` user. However, you can view them using the following:
    
    
    USE msdb
    select * from dbo.sysjobs
    

#### Publishers missing in the Replication Monitor

You can use the [Replication monitor](https://docs.microsoft.com/en-us/sql/relational-databases/replication/monitor/start-the-replication-monitor?view=sql-server-ver15) to view the status of replication and to troubleshoot replication issues.

For example, when you set up replication and your publisher Cloud SQL instance uses an IP address, SSMS may be unable to find the publisher. This is because it does not know the mapping between the hostname and the IP address.

The Replication Monitor contains an empty Publications tab:

![No rows are in the Publications tab](https://docs.cloud.google.com/static/sql/images/publisher-empty-pub-tab.png)

As a workaround, you can [create aliases](https://docs.microsoft.com/en-us/sql/database-engine/configure-windows/create-or-delete-a-server-alias-for-use-by-a-client?view=sql-server-ver15#:%7E:text=To%20create%20an%20alias,IP%20address%20of%20a%20server.) in the [SQL Server Configuration Manager](https://docs.microsoft.com/en-us/sql/relational-databases/sql-server-configuration-manager?view=sql-server-ver15) between the SQL Server hostname of the publisher and the IP address used to connect from SSMS:

  1. Start the SQL Server Configuration Manager.

![SQL Server Configuration Manager](https://docs.cloud.google.com/static/sql/images/publisher-config-manager.png)

  2. Find the **Aliases** node and select it.

![Aliases node is selected](https://docs.cloud.google.com/static/sql/images/publisher-aliases-node.png)

  3. Right-click the box under **Alias name** to create a new alias. The same procedure applies for both a 32-bit alias and a 64-bit alias:

![Drop-down box under Alias name](https://docs.cloud.google.com/static/sql/images/publisher-new-alias.png)

  4. Retrieve the actual hostname of your publisher instance using this query:

![Query for the actual hostname of your publisher instance](https://docs.cloud.google.com/static/sql/images/publisher-hostname.png)

  5. In the alias window, enter these fields before selecting **OK** :

**Alias Name** : Provide the server name from the query in Step 4.

**Port No:** Provide port 1433.

**Protocol:** Leave the value as the default of TCP/IP.

**Server:** Provide the IP address of the Publisher instance.

![Values for the alias name, server, etc.](https://docs.cloud.google.com/static/sql/images/publisher-server-name.png)

  6. Connect using the new alias, and launch the Replication Monitor:

![Connect to Server dialog box](https://docs.cloud.google.com/static/sql/images/publisher-connect-to-server.png)




The publishing information should be similar to the following:

![Replication Monitor now displays a row in the Publications tab](https://docs.cloud.google.com/static/sql/images/publisher-publishing-info.png)

For more information about troubleshooting replication, see [Troubleshooter: Find errors with SQL Server transactional replication](https://docs.microsoft.com/en-us/sql/relational-databases/replication/troubleshoot-tran-repl-errors?view=sql-server-ver15).

#### Estimating the size of articles needed for replication

When you use a Cloud SQL instance as a publisher, an initial snapshot of the articles to be generated is necessary to begin replication. This snapshot is stored locally. Depending on the number of articles, their size, and the type of data, the storage requirements may increase. The `sp_spaceused` stored procedure provides only a rough estimate of the disk space needed for an article.

The snapshot includes files that store schemas and data.

## What's next

  * Learn [about replication in Cloud SQL](https://docs.cloud.google.com/sql/docs/sqlserver/replication).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
