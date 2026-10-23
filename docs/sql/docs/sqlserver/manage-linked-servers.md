---
url: https://docs.cloud.google.com/sql/docs/sqlserver/manage-linked-servers/
title: Manage linked servers \u00a0|\u00a0 Cloud SQL for SQL Server \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:12:14.471262+00:00
---

# Manage linked servers  |  Cloud SQL for SQL Server  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/sqlserver/manage-linked-servers/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ SQL Server ](https://docs.cloud.google.com/sql/docs/sqlserver)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/sqlserver/features)



Send feedback 

#  Manage linked servers Stay organized with collections  Save and categorize content based on your preferences. 

MySQL | PostgreSQL | SQL Server

Linked servers let you read data and execute commands across external SQL Server databases from Cloud SQL. After you enroll your instance, you can configure encrypted connections, map user logins, and run distributed queries or remote procedure calls (RPC).

## Enroll your instance to allow linked servers

To add the `cloudsql enable linked servers` flag to your instance, use the following command:
    
    
    gcloud sql instances patch INSTANCE_NAME --database-flags="cloudsql enable linked servers"=on

Replace `INSTANCE_NAME` with the name of the instance that you want to use for linking servers.

For more information, see [configure database flags](https://docs.cloud.google.com/sql/docs/sqlserver/flags#config).

## Add a linked server

To add a linked server, run the Transact-SQL `sp_addlinkedserver` command:
    
    
    EXEC master.dbo.sp_addlinkedserver
        @server = N'LINKED_SERVER_NAME',
        @srvproduct=N'',
        @provider=N'MSOLEDBSQL',
        @datasrc=N'TARGET_SERVER_ID'

Replace the following:

  * LINKED_SERVER_NAME with the name of the linked server to create.
  * TARGET_SERVER_ID with the network name, DNS name, or IP address for the linked server. For the instance name, use the format `servername\instancename`. If your instance uses a non-standard port, add the port number. For example, `servername\instancename, 8080`.



To add user mapping for a user who is logged in, run the following command:
    
    
    EXEC master.dbo.sp_addlinkedsrvlogin
        @rmtsrvname=N'LINKED_SERVER_NAME',
        @useself=N'True'

Replace LINKED_SERVER_NAME with the name of the linked server.

To create or update the default remote login and password, and apply it to all local logins, run the following command:
    
    
    EXEC master.dbo.sp_addlinkedsrvlogin
        @rmtsrvname=N'LINKED_SERVER_NAME',
        @useself=N'False',
        @locallogin=N'LOGIN',
        @rmtuser=N'USER_ID',
        @rmtpassword='PASSWORD';

Replace the following:

  * LINKED_SERVER_NAME with the name of the linked server.
  * LOGIN with the login for the local server. `locallogin` is sysname, with a default of NULL. NULL specifies that this entry applies to all local logins that connect to `rmtsrvname`. If not NULL, `locallogin` is either a SQL Server login or a Windows login. If you use a Windows login, it must have access to the SQL Server either directly, or through its membership in a Windows group that has access.
  * USER_ID with the user logging in.
  * PASSWORD with the user password.



## Add a linked server with an encrypted connection

To add a linked server using an encrypted connection, run the Transact-SQL `sp_addlinkedserver` command:
    
    
    EXEC master.dbo.sp_addlinkedserver
        @server = N'LINKED_SERVER_NAME',
        @srvproduct=N'',
        @provider=N'MSOLEDBSQL',
        @datasrc=N'TARGET_SERVER_ID,
        @provstr=N'Encrypt=yes;'

Replace the following:

  * LINKED_SERVER_NAME with the name of the linked server to create.
  * TARGET_SERVER_ID with the name of the target server, or the IP address and port number for the target server.



If the name of the server is different from the name in the certificate, you need to indicate that the SQL Server can trust the server certificate. To update the provider string, run the following command:
    
    
    EXEC master.dbo.sp_addlinkedserver
        @server = N'LINKED_SERVER_NAME',
        @srvproduct=N'',
        @provider=N'MSOLEDBSQL',
        @datasrc=N'TARGET_SERVER_ID,
        @provstr=N'Encrypt=yes;TrustServerCertificate=yes;'

Replace the following:

  * LINKED_SERVER_NAME with the name of the linked server to create.
  * TARGET_SERVER_ID with the name of the target server, or the IP address and port number for the target server.



## Linked server queries

Cloud SQL supports the use of four-part names to query linked servers (server name, database name, schema name, and object name), in addition to the following commands:

  * [OPENQUERY](https://learn.microsoft.com/en-us/sql/t-sql/functions/openquery-transact-sql?view=sql-server-ver16) executes a query on a specified server.
  * [EXECUTE](https://learn.microsoft.com/en-us/sql/t-sql/language-elements/execute-transact-sql?view=sql-server-ver16) lets you run dynamic SQL against a linked server.

**Note:** Cloud SQL doesn't support `OPENROWSET` as a way to query a linked server.

For more information, see [Compare query remote execution options](https://learn.microsoft.com/en-us/sql/relational-databases/linked-servers/linked-servers-openquery-openrowset-exec-at?view=sql-server-ver16).

## Enable remote procedure calls on a linked server

Remote procedure calls (RPC) let you run stored procedures on linked servers. To add RPC, you run the Transact-SQL [`sp_serveroption`](https://learn.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/sp-serveroption-transact-sql?view=sql-server-ver16) command with an RPC argument. There are two RPC arguments:

  * `rpc` enables RPC from the specified server.
  * `rpc out` enables RPC to the specified server.



Use the following `sp_serveroption` command with the `rpc` argument to enable RPC from LINKED_SERVER_NAME:
    
    
    EXEC sp_serveroption
        @server='LINKED_SERVER_NAME',
        @optname='rpc',
        @optvalue='TRUE'

Replace LINKED_SERVER_NAME with the name of the linked server.

Use the following `sp_serveroption` command with the `rpc out` argument to enable RPC:
    
    
    EXEC sp_serveroption
        @server='LINKED_SERVER_NAME',
        @optname='rpc out',
        @optvalue='TRUE'

Replace LINKED_SERVER_NAME with the name of the linked server.

## Remove the user mapping for a linked server

To remove a user mapping that you previously added, run the following command:
    
    
    EXEC master.dbo.sp_droplinkedsrvlogin
        @rmtsrvname=N'LINKED_SERVER_NAME',
        @locallogin=N'LOGIN';

Replace the following:

  * LINKED_SERVER_NAME with the name of the linked server to drop.
  * LOGIN with the login for the local server. `locallogin` is sysname, with a default of NULL. NULL specifies that this entry applies to all local logins that connect to `rmtsrvname`. If not NULL, `locallogin` is either a SQL Server login or a Windows login. If you use a Windows login, it must have access to the SQL Server either directly, or through its membership in a Windows group that has access.



## Remove an enrolled instance from allowing linked servers

To remove linked servers, do the following:

  * Drop existing linked servers with the Transact-SQL [sp_dropserver](https://learn.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/sp-dropserver-transact-sql?view=sql-server-ver16) stored procedure.
  * Remove the `cloudsql enable linked servers` flag to remove an enrolled instance.
        
        gcloud sql instances patch INSTANCE_NAME --database-flags="cloudsql enable linked servers"=off

Replace `INSTANCE_NAME` with the name of the instance where you want to remove linked servers.

Alternatively, you can run the following command to clear all database flags:
        
        gcloud sql instances patch INSTANCE_NAME --clear-database-flags

Replace `INSTANCE_NAME` with the name of the instance where you want to remove linked servers.




## Troubleshoot

Issue | Troubleshooting  
---|---  
`Msg 7411, Level 16, State 1, Line 25  
  
Server 'LINKED_SERVER_NAME' is not configured for DATA ACCESS.` | The `DataAccess` option is disabled. Run the following command to enable data access:  

    
    
    EXEC sp_serveroption
        @server='LINKED_SERVER_NAME',
        @optname='data access',
        @optvalue='TRUE'

Replace LINKED_SERVER_NAME with the name of the linked server.   
`Access to the remote server is denied because no login-mapping exists. (Microsoft SQL Server, Error: 7416)` | If you have this issue while establishing an encrypted connection, you need to try another way to provide the user ID when you access the linked server. To do this, run the following command: 
    
    
    EXEC master.dbo.sp_addlinkedserver
       @server = N'LINKED_SERVER_NAME',
       @srvproduct= N'',
       @provider= N'MSOLEDBSQL',
       @datasrc= N'TARGET_SERVER_ID',
       @provstr= N'Encrypt=yes;TrustServerCertificate=yes;User ID=USER_ID'

Replace the following:  


  * LINKED_SERVER_NAME with the name of the linked server.
  * TARGET_SERVER_ID with the name of the target server, or the IP address and port number for the target server.
  * USER_ID with the user logging in.

  
Unexpected behavior  | If you experience unexpected behavior, make sure you're using a supported provider. For more information, see the [Microsoft documentation](https://learn.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/sp-addlinkedserver-transact-sql?view=sql-server-linux-ver16#----nprovider).   
  
## What's next

  * Learn about [using linked servers](https://docs.cloud.google.com/sql/docs/sqlserver/linked-servers).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
