---
url: https://docs.cloud.google.com/looker/docs/db-config-oracle-autonomous-data-warehouse/
title: Oracle Autonomous Data Warehouse on Cloud \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:25:14.979704+00:00
---

# Oracle Autonomous Data Warehouse on Cloud  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/db-config-oracle-autonomous-data-warehouse/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  Oracle Autonomous Data Warehouse on Cloud Stay organized with collections  Save and categorize content based on your preferences. 

Looker has [integration-level support](https://docs.cloud.google.com/looker/docs/dialects#support_levels_and_jdbc_installation) for Oracle ADWC. This page contains information about connecting Looker to Oracle ADWC.

## Encrypting network traffic

It is a best practice to encrypt network traffic between the Looker application and your database. Consider one of the options that are described on the [Enabling secure database access](https://docs.cloud.google.com/looker/docs/enabling-secure-db-access) documentation page.

## Setting up the Looker host for connections

All Oracle ADWC connections require [SSL and certificate authentication](https://docs.oracle.com/en/cloud/paas/autonomous-data-warehouse-cloud/user/connect-intorduction.html#GUID-CD4C10A6-1C1E-4969-8F67-1433B6CE626A). In order for Looker to connect to your Oracle ADWC instance, it is necessary to [download your Oracle wallet](https://docs.oracle.com/en/cloud/paas/autonomous-data-warehouse-cloud/user/connect-download-wallet.html#GUID-B06202D2-0597-41AA-9481-3B174F75D4B1) files and install them on the Looker server. If you are a customer-hosted Looker user, you will need a system administrator with access to the Looker server to do this. If you are a Looker-hosted user, reach out to Looker Support.

To install your Oracle wallet on the Looker server:

  1. [Download your Oracle wallet](https://docs.oracle.com/en/cloud/paas/autonomous-data-warehouse-cloud/user/connect-download-wallet.html#GUID-B06202D2-0597-41AA-9481-3B174F75D4B1) to your **local** computer. You will have a zip file named something like `Wallet_databasename.zip`.

  2. On the Looker server, make a directory to hold the wallet zip file:
         
         mkdir /home/looker/looker/credentials
         

  3. Copy the wallet zip file from your local computer to the Looker server. This example uses `scp` and places the file in `/home/looker/looker/credentials`:
         
         scp Wallet_databasename.zip username@remotehost:/home/looker/looker/credentials
         

  4. Unzip the wallet zip file. This example uses the command `unzip`:
         
         cd /home/looker/looker/credentials
         unzip Wallet_databasename.zip
         

  5. Verify the contents of the wallet with the `ls` command. These are the files you should have:
         
         ls
         
          cwallet.sso  keystore.jks      sqlnet.ora    truststore.jks
          ewallet.p12  ojdbc.properties  tnsnames.ora
         

Looker connects to Oracle ADWC using Oracle Wallets with the [JDBC Thin Driver 18.3](https://docs.oracle.com/en/cloud/paas/autonomous-data-warehouse-cloud/user/connect-jdbc-thin-wallet.html#GUID-20656D84-4D79-4EE9-B55F-333053948966). For this, you will need the Transparent Network Substrate (TNS) Alias of the Oracle ADWC Service level for your database and the PATH to your Oracle wallet files.

  6. To get the TNS Alias of your database, run this command:
         
         cat tnsnames.ora
         

There will be three TNS aliases to choose from: `dbname_high`, `dbname_medium`, and `dbname_low`. These aliases correspond to different levels of service. The protocol, host, port, service name, and SSL information is included in this file. For this example, we will use `dbname_medium`.




## Creating a Looker user

First, create a designated Looker user:
    
    
      -- connect / as sysdba;
      CREATE USER LOOKER IDENTIFIED BY <password>
      DEFAULT TABLESPACE USERS
      TEMPORARY TABLESPACE TEMP;
    

Next, give the new Looker user the ability to create sessions:
    
    
      GRANT CREATE SESSION TO LOOKER;
    

Finally, give the Looker user the appropriate `SELECT` permissions for the data tables that you plan to access from Looker. If you want to access additional tables in the future, you will need to grant `SELECT` on those new tables as well.
    
    
      GRANT SELECT ON -- <all tables that will be used by looker>;
    

## Ensuring that Looker can see all tables

Looker may not be able to identify tables (especially empty tables) without first collecting statistics in Oracle. If tables you need don't appear in generated LookML or SQL Runner, execute this command:
    
    
      EXEC DBMS_STATS.GATHER_DATABASE_STATS;
    

For alternative methods, consult your Oracle documentation.

## Setting up main database objects

Your Oracle DBA must set up the following objects and permissions on Oracle. The following commands create `LOOKER_SESSION` and `LOOKER_SQL` as synonyms for `V$SESSION` and `V$SQL`.

Run the following commands as the root user to complete this setup. These examples assume that the Looker user's name is `LOOKER`.
    
    
    CREATE OR REPLACE VIEW LOOKER_SQL
    AS
      SELECT
        sql.SQL_ID,
        sql.SQL_TEXT
      FROM
        V$SQL sql,
        v$session sess
      WHERE
        sess.SQL_ADDRESS = sql.ADDRESS AND
        sess.username=&apos;LOOKER&apos;;
    
    CREATE OR REPLACE SYNONYM LOOKER.LOOKER_SQL FOR LOOKER_SQL;
    
    GRANT SELECT ON LOOKER.LOOKER_SQL TO LOOKER;
    
    -- Pay special attention to the comments:
    -- the following view will be different for clustered Oracle deployments
    CREATE OR REPLACE VIEW LOOKER_SESSION
    AS
      SELECT
        SID,
        USERNAME,
        TYPE,
        STATUS,
        SQL_ID,
        -- If using a single node Oracle ADWC deployment
        "SERIAL#",
        -- If using a clustered Oracle ADWC deployment
        (SERIAL# || ',' || INST_ID) AS "SERIAL#",
        AUDSID
      -- If using a single node Oracle ADWC deployment
      FROM V$SESSION
      -- If using a clustered Oracle ADWC deployment
      FROM GV$SESSION
      WHERE
        USERNAME=&apos;LOOKER&apos;;
    
    CREATE OR REPLACE SYNONYM LOOKER.LOOKER_SESSION FOR LOOKER_SESSION;
    
    GRANT SELECT ON LOOKER.LOOKER_SESSION TO LOOKER;
    

## Setting up symmetric aggregates

Your Oracle DBA must set up the `LOOKER_HASH` function to enable [symmetric aggregates](https://docs.cloud.google.com/looker/docs/reference/param-explore-symmetric-aggregates). The `LOOKER_HASH` function is a synonym for the Oracle `dbms_crypto.hash` function. The DBA must also create the associated synonym and privileges. The following example assumes that the Looker user's name is `LOOKER`:
    
    
    CREATE OR REPLACE FUNCTION LOOKER_HASH(bytes raw, prec number)
      RETURN raw AS
        BEGIN
      return(dbms_crypto.HASH(bytes, prec));
    END;
    
    CREATE OR REPLACE SYNONYM LOOKER.LOOKER_HASH FOR LOOKER_HASH;
    
    GRANT EXECUTE ON LOOKER.LOOKER_HASH TO LOOKER;
    
    GRANT EXECUTE ON SYS.LOOKER_HASH TO LOOKER;
    

> Depending on your Oracle database configuration, the `SYS` prefix may be `SYSDBA`, `ADMIN`, or unnecessary.

## Setting up persistent derived tables

To enable [persistent derived tables](https://docs.cloud.google.com/looker/docs/derived-tables#persistent-derived-tables), give the Looker user the `UNLIMITED TABLESPACE` and `CREATE TABLE` permissions. The following commands assume that the Looker user's name is `LOOKER`:
    
    
    GRANT UNLIMITED TABLESPACE TO LOOKER;
    GRANT CREATE TABLE TO LOOKER;
    

## Setting up query killing

To set up query killing, the Oracle DBA must create the `LOOKER_KILL_QUERY` procedure as a synonym of `ALTER SYSTEM KILL SESSION`. To do this, execute the following command:
    
    
    CREATE OR REPLACE PROCEDURE LOOKER_KILL_QUERY(p_sid in varchar2,
                                                  p_serial# in varchar2)
    IS
      cursor_name pls_integer default dbms_sql.open_cursor;
      ignore pls_integer;
    
    BEGIN
      SELECT
        COUNT(*) INTO IGNORE
      -- If using a single node Oracle ADWC deployment
      FROM V$SESSION
      -- If using a clustered Oracle ADWC deployment
      FROM GV$SESSION
      WHERE
        username = USER
        AND sid = p_sid
        -- If using a single node Oracle ADWC deployment
        AND serial# = p_serial#;
        -- If using a clustered Oracle ADWC deployment
        AND (SERIAL# || ',' || INST_ID) = p_serial#;
    
      IF (ignore = 1)
      THEN
        dbms_sql.parse(cursor_name,
                       &apos;ALTER SYSTEM KILL SESSION &apos;&apos;&apos;
                       || p_sid || &apos;,&apos; || p_serial# || &apos;&apos;&apos;&apos;,
                       dbms_sql.native);
        ignore := dbms_sql.execute(cursor_name);
      ELSE
        raise_application_error(-20001,
                                &apos;You do not own session &apos;&apos;&apos; ||
                                p_sid || &apos;,&apos; || p_serial# ||
                                &apos;&apos;&apos;&apos;);
      END IF;
    END;
    

The DBA will also need to run these related commands:
    
    
    CREATE OR REPLACE SYNONYM LOOKER.LOOKER_KILL_QUERY FOR SYS.LOOKER_KILL_QUERY;
    GRANT EXECUTE ON SYS.LOOKER_KILL_QUERY TO LOOKER;
    

> Depending on your Oracle database configuration, the `SYS` prefix may be `SYSDBA`, `ADMIN`, or unnecessary.

## Creating the Looker connection to your database

Follow these steps to create the connection from Looker to your database:

  1. In the **Admin** section of Looker, select **Connections** , and then click **Add Connection**.
  2. Fill out the connection details. The majority of the settings are common to most database dialects. See the [Connecting Looker to your database](https://docs.cloud.google.com/looker/docs/connecting-to-your-db) documentation page for information. The following settings are specific to Oracle ADWC:

     * **Dialect** : **Oracle ADWC**.
**Note:** If you are on a [Looker (Google Cloud core)](https://docs.cloud.google.com/looker/docs/looker-core-overview) instance and you don't see your dialect listed in the **Dialect** drop-down menu, see the [Looker (Google Cloud core) documentation](https://docs.cloud.google.com/looker/docs/looker-core-dialects#supported_dialects_for) to verify that the dialect is supported for Looker (Google Cloud core) instances.
     * **Use TNS** : Enable Transparent Network Substrate (TNS) connections.
     * **Host** : Hostname or TNS alias. For this example, `dbname_medium`.
     * **Port** : Leave as default; Looker will find the port from the `tnsnames.ora` file.
     * **Service Name** : Leave blank; Looker will find the service name from the `tnsnames.ora` file.
     * **Username** : Database username or **Temp Database** if PDTs are enabled.
     * **Password** : Database user password.
     * **Enable PDTs** : Use this toggle to enable [persistent derived tables](https://docs.cloud.google.com/looker/docs/derived-tables#persistent-derived-tables). When PDTs are enabled, the **Connection** window reveals additional PDT settings and the [**PDT Overrides**](https://docs.cloud.google.com/looker/docs/connecting-to-your-db#pdt-overrides) section.
     * **Temp Database**: In Oracle, _a user is a schema_ , so this should be specified as the name of the database user. For this example, you would use the temp schema value `LOOKER`.
     * **Additional JDBC parameters** : Leave this blank, since Oracle does not support additional JDBC parameters.
     * **SSL and Verify SSL** : You can ignore these fields; Looker will always use SSL with Oracle ADWC.
  3. To verify that the connection is successful, click the **Test Connection** button in the **Status details** section at the bottom of the **Connections Settings** page.

  4. If Looker displays **Can Connect** , press **Connect** to create the connection. 




Your database connection is then added to the list on the Looker [**Connections**](https://docs.cloud.google.com/looker/docs/admin-panel-database-connections) **Admin** page.

## Feature support

For Looker to support some features, your database dialect must also support them.

Oracle ADWC supports the following features as of Looker 26.20:

Feature | Supported?  
---|---  
Looker (Google Cloud core)|   
Symmetric aggregates|   
Derived tables|   
Persistent SQL derived tables|   
Persistent native derived tables|   
Stable views|   
Query killing|   
SQL-based pivots|   
Time zones|   
SSL|   
Subtotals|   
JDBC additional params|   
Case-sensitive|   
Location type|   
List type|   
Percentile|   
Distinct percentile|   
SQL Runner Show Processes|   
SQL Runner Describe Table|   
SQL Runner Show Indexes|   
SQL Runner Select 10|   
SQL Runner Count|   
SQL Explain|   
OAuth 2.0 credentials|   
Context comments|   
Connection pooling|   
HLL sketches|   
Aggregate awareness|   
Incremental PDTs|   
Milliseconds|   
Microseconds|   
Materialized views|   
Period-over-period measures|   
Approximate count distinct|   
In-database analytic models|   
Custom calendars|   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
