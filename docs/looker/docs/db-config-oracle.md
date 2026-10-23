---
url: https://docs.cloud.google.com/looker/docs/db-config-oracle/
title: Oracle \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:35:01.584087+00:00
---

# Oracle  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/db-config-oracle/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  Oracle Stay organized with collections  Save and categorize content based on your preferences. 

You can configure Looker to analyze data stored in your Oracle database. Looker's Oracle integration provides a secure connection, supports persistent derived tables (PDTs), and facilitates query termination. Through this integration, you can use your Oracle data directly within the Looker platform to support your analysis and operational needs.

**Note:** Looker support for Oracle is implemented using standard Oracle deployments. If your Oracle database is and [Oracle RAC](https://www.oracle.com/database/technologies/rac.html) deployment, Looker can connect successfully. However, Looker might encounter issues canceling queries because of a difference in metadata for retrieving query connection IDs from nodes.

## Encrypting network traffic

It is a best practice to encrypt network traffic between the Looker application and your database. Consider one of the options that are described on the [Enabling secure database access](https://docs.cloud.google.com/looker/docs/enabling-secure-db-access) documentation page.

If you're interested in using SSL encryption, see the [Oracle documentation](https://docs.oracle.com/database/121/DBSEG/asossl.htm#DBSEG070%20on%20configuring%20SSL%20authentication).

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
    

## Ensuring Looker can see all tables

Looker may not be able to identify tables (especially empty tables) without first collecting statistics in Oracle. If tables you need do not appear in generated LookML or SQL Runner, try executing:
    
    
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
        sess.username='LOOKER';
    
    CREATE OR REPLACE SYNONYM LOOKER.LOOKER_SQL FOR LOOKER_SQL;
    
    GRANT SELECT ON LOOKER.LOOKER_SQL TO LOOKER;
    
    -- Pay special attention to the following comments:
    -- the following view will be different for clustered Oracle deployments
    CREATE OR REPLACE VIEW LOOKER_SESSION
    AS
      SELECT
        SID,
        USERNAME,
        TYPE,
        STATUS,
        SQL_ID,
        -- If using a single node Oracle deployment
        "SERIAL#",
        -- If using a clustered Oracle deployment, like Oracle Real Application Clusters
        (SERIAL# || ',' || INST_ID) AS "SERIAL#",
        AUDSID
      -- If using a single node Oracle deployment
      FROM V$SESSION
      -- If using a clustered Oracle deployment, like Oracle Real Application Clusters
      FROM GV$SESSION
      WHERE
        USERNAME='LOOKER';
    
    CREATE OR REPLACE SYNONYM LOOKER.LOOKER_SESSION FOR LOOKER_SESSION;
    
    GRANT SELECT ON LOOKER.LOOKER_SESSION TO LOOKER;
    

## Setting up symmetric aggregates

Your Oracle DBA must set up the `LOOKER_HASH` function to enable [symmetric aggregates](https://docs.cloud.google.com/looker/docs/reference/param-explore-symmetric-aggregates). The `LOOKER_HASH` function is a synonym for the Oracle `dbms_crypto.hash` function. The DBA must also create the associated synonym and privileges. The following commands assume that the Looker user's name is `LOOKER`:

**Note:** The error `ORA-00904: "LOOKER_HASH": invalid identifier` indicates that the LOOKER_HASH function, which is required for symmetric aggregates, does not exist in your database. This would be expected if one skipped the symmetric aggregates setup which would have created this function.
    
    
    CREATE OR REPLACE FUNCTION LOOKER_HASH(bytes raw, prec number)
      RETURN raw AS
      BEGIN
        return(dbms_crypto.HASH(bytes, prec));
      END;
    
    CREATE OR REPLACE SYNONYM LOOKER.LOOKER_HASH FOR LOOKER_HASH;
    
    GRANT EXECUTE ON LOOKER.LOOKER_HASH TO LOOKER;
    
    GRANT EXECUTE ON SYS.LOOKER_HASH TO LOOKER;
    

**Note:** Depending on your Oracle database configuration, the `SYS` prefix may be `SYSDBA`, `ADMIN`, or unnecessary.

## Setting up persistent derived tables

To enable [persistent derived tables](https://docs.cloud.google.com/looker/docs/derived-tables#persistent-derived-tables), give the Looker user the `UNLIMITED TABLESPACE` and `CREATE TABLE` permissions. The following commands assume that the Looker user's name is `LOOKER`:
    
    
    GRANT UNLIMITED TABLESPACE TO LOOKER;
    GRANT CREATE TABLE TO LOOKER;
    

## Setting up query killing

Follow these instructions to configure query killing for either a standard Oracle deployment or an Amazon RDS deployment.

**Note:** During a connection test, if you see the error `Test kill failed - Cannot cancel queries: undefined method '[]' for nil:NilClass`, the error could be linked to incorrectly configured permissions for query killing. The error may indicate that the necessary grants are not applied correctly to the database user specified in the Looker connection settings, or that the necessary grants are not applied not at all.

### Standard Oracle deployments

To set up query killing in standard Oracle deployments, the Oracle DBA must create the `LOOKER_KILL_QUERY` procedure as a synonym of `ALTER SYSTEM KILL SESSION`. To do this, execute the following command:
    
    
    CREATE OR REPLACE PROCEDURE LOOKER_KILL_QUERY(p_sid in varchar2,
                                                  p_serial# in varchar2)
    IS
      cursor_name pls_integer default dbms_sql.open_cursor;
      ignore pls_integer;
    
    BEGIN
      SELECT
        COUNT(*) INTO ignore
      -- If using a single node Oracle deployment
      FROM V$SESSION
      -- If using a clustered Oracle deployment, like Oracle Real Application Clusters
      FROM GV$SESSION
      WHERE
        username = USER
        AND sid = p_sid
        -- If using a single node Oracle deployment
        AND serial# = p_serial#;
        -- If using a clustered Oracle deployment, like Oracle Real Application Clusters
        AND (SERIAL# || ',' || INST_ID) = p_serial#;
    
      IF (ignore = 1)
      THEN
        dbms_sql.parse(cursor_name,
                       'ALTER SYSTEM KILL SESSION '''
                       || p_sid || ',' || p_serial# || '''',
                       dbms_sql.native);
        ignore := dbms_sql.execute(cursor_name);
      ELSE
        raise_application_error(-20001,
                                'You do not own session ''' ||
                                p_sid || ',' || p_serial# ||
                                '''');
      END IF;
    END;
    

The DBA will also need to run these related commands:
    
    
    CREATE OR REPLACE SYNONYM LOOKER.LOOKER_KILL_QUERY FOR SYS.LOOKER_KILL_QUERY;
    GRANT EXECUTE ON SYS.LOOKER_KILL_QUERY TO LOOKER;
    

**Note:** Depending on your Oracle database configuration, the `SYS` prefix may be `SYSDBA`, `ADMIN`, or unnecessary.

### Amazon RDS deployments

In Amazon RDS Oracle deployments, the [`rdsadmin.rdsadmin_util.kill`](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.Oracle.CommonDBATasks.KillingSession.html) procedure is used to kill queries. To use this procedure, the Looker database user must have the `DBA` role assigned.

**Note:** Because DBA is an elevated database role, you might consider skipping this step and forgoing query killing in Looker.

To give the Looker database user query killing abilities, run the following command:
    
    
    GRANT DBA TO LOOKER;
    

## Creating the Looker connection to your database

In the **Admin** section of Looker, select **Connections** , and then click **Add Connection**.

Fill out the connection details. The majority of the settings are common to most database dialects. See the [Connecting Looker to your database](https://docs.cloud.google.com/looker/docs/connecting-to-your-db) documentation page for information. The following settings are specific to Oracle:

  * **Name** : Specify the name of the connection. This is how you will refer to the connection in LookML projects.
  * **Dialect** : Oracle.
  * **Use TNS** : Enable Transparent Network Substrate (TNS) connections.
  * **Host** : Hostname or TNS alias.
  * **Port** : Database port.
  * **Database** : Database name (if not using TNS).
  * **Service Name** : Service name (if using TNS).
  * **Username** : Database username or **Temp Database** if PDTs are enabled.
  * **Password** : Database user password.
  * **Enable PDTs** : Use this toggle to enable [persistent derived tables](https://docs.cloud.google.com/looker/docs/derived-tables#persistent-derived-tables). When PDTs are enabled, the **Connection** window reveals additional PDT settings and the [**PDT Overrides**](https://docs.cloud.google.com/looker/docs/connecting-to-your-db#pdt-overrides) section.
  * **Temp Database**: In Oracle _a user is a schema_ , so this should be specified as the name of the database user. For this example, you would use the temp schema value `LOOKER`.
  * **Max number of PDT builder connections** : Specify the number of possible concurrent PDT builds on this connection. Setting this value too high could negatively impact query times. For more information, see the [Connecting Looker to your database](https://docs.cloud.google.com/looker/docs/connecting-to-your-db#max_pdt_builder_connections) documentation page.
  * **Additional JDBC parameters** : Leave this blank, since Oracle does not support additional JDBC parameters.
  * **Maintenance Schedule** : A [`cron`](https://en.wikipedia.org/wiki/Cron#CRON_expression) expression that indicates when Looker should check [datagroups](https://docs.cloud.google.com/looker/docs/caching-and-datagroups#specifying_caching_policies_with_datagroup_parameters) and persistent derived tables. Read more about this setting in the [Maintenance Schedule](https://docs.cloud.google.com/looker/docs/connecting-to-your-db#pdt_maintenance_schedule) documentation.
  * **SSL** : Check to use SSL connections.
  * **Verify SSL** : Ignore this field. Oracle will use the default Java Truststore to verify SSL.
  * **Max connections per node** : This setting can be left at the default value initially. Read more about this setting in the [Max connections per node](https://docs.cloud.google.com/looker/docs/connecting-to-your-db#max_connections) section of the **Connecting Looker to your database** documentation page.
  * **Connection Pool Timeout** : This setting can be left at the default value initially. Read more about this setting in the [Connection Pool Timeout](https://docs.cloud.google.com/looker/docs/connecting-to-your-db#connection-pool-timeout) section of the **Connecting Looker to your database** documentation page.
  * **SQL Runner Precache** : To cause SQL Runner not to preload table information and to load table information only when a table is selected, uncheck this option. Read more about this setting in the [SQL Runner Precache](https://docs.cloud.google.com/looker/docs/connecting-to-your-db#sql_runner_precache) section of the **Connecting Looker to your database** documentation page.
  * **Database Time Zone** : Specify the time zone used in the database. Leave this field blank if you do not want time zone conversion. See the [Using time zone settings](https://docs.cloud.google.com/looker/docs/using-time-zone-settings) documentation page for more information.



To verify that the connection is successful, click the **Test Connection** button in the **Status details** section at the bottom of the **Connections Settings** page.

If Looker displays **Can Connect** , press **Connect** to create the connection. 

Your database connection is then added to the list on the Looker [**Connections**](https://docs.cloud.google.com/looker/docs/admin-panel-database-connections) **Admin** page.

## Feature support

For Looker to support some features, your database dialect must also support them.

Oracle supports the following features as of Looker 26.20:

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

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
