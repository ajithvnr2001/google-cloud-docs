---
url: https://docs.cloud.google.com/looker/docs/db-config-exasol/
title: Exasol \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:42:44.346544+00:00
---

# Exasol  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/db-config-exasol/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  Exasol Stay organized with collections  Save and categorize content based on your preferences. 

## Encrypting network traffic

It is a best practice to encrypt network traffic between the Looker application and your database. Consider one of the options that are described on the [Enabling secure database access](https://docs.cloud.google.com/looker/docs/enabling-secure-db-access) documentation page.

The Exasol JDBC drivers support encrypted connections. If you're interested, see [Exasol's documentation](https://docs.exasol.com/connect_exasol/drivers/jdbc.htm).

## Create a Looker user

First, create a designated Looker user and give it the ability to create sessions:
    
    
    CREATE USER LOOKER IDENTIFIED BY "<password>";
    GRANT CREATE SESSION TO LOOKER;
    

**Note:** Put the password in double quotes. Otherwise, it will be stored as case-insensitive; _ChangeIt_ will be stored as _CHANGEIT_.

Give the Looker user the appropriate `SELECT` permissions for the schema or tables that you plan to access from Looker:
    
    
    GRANT SELECT ON <tables that will be used by LOOKER>;
    

Alternatively, you can grant all privileges:
    
    
    GRANT ALL PRIVILEGES ON SCHEMA <YOUR_SCHEMA> TO LOOKER;
    

Alternatively, if you don't want to have to re-run `GRANT` statements on newly created tables in the future:
    
    
    GRANT SELECT ANY TABLE TO LOOKER;
    

## Persistent derived tables

If you want to enable [PDTs](https://docs.looker.com/data-modeling/learning-lookml/derived-tables#adding_persistence) for your Looker connection to Exasol, run this command:
    
    
    CREATE SCHEMA LOOKER_SCRATCH;
    ALTER SCHEMA LOOKER_SCRATCH CHANGE OWNER LOOKER;
    

Alternatively, you can grant all privileges:
    
    
    GRANT ALL PRIVILEGES ON SCHEMA LOOKER_SCRATCH TO LOOKER;
    

## Enable symmetric aggregates

To allow Exasol to take advantage of [symmetric aggregates](https://docs.cloud.google.com/looker/docs/best-practices/understanding-symmetric-aggregates), create the `hexstring2dec` function:
    
    
    OPEN SCHEMA <YOUR_SCHEMA>;
    
    create or replace function hexstring2dec(hexstring in varchar(32)) return decimal(36,0)
    is
        pos smallint;
        current_hexstring char(1);
        current_hexstring_dec smallint;
        hexstring_length smallint;
        res decimal(36,0);
    begin
        if hexstring is null then
            return null;
        end if;
        hexstring_length := length(hexstring);
        res := 0;
        pos := 1;
        while  pos <= hexstring_length
        do
            current_hexstring := substr(hexstring,pos,1);
            if current_hexstring in ('A','B','C','D','E','F') then
                current_hexstring_dec := ascii(current_hexstring) - ascii('A') + 10;
            else
                current_hexstring_dec := to_number(current_hexstring);
            end if;
            res := (res * 16) + current_hexstring_dec;
            pos := pos + 1;
        end while;
        return res;
    end hexstring2dec;
    /
    
    GRANT EXECUTE ON FUNCTION hexstring2dec;
    

## Creating the Looker connection to your database

Follow these steps to create the connection from Looker to your database:

  1. In the **Admin** section of Looker, select **Connections** , and then click **Add Connection**.
  2. Select **Exasol** from the **Dialect** drop-down menu.

**Note:** If you are on a [Looker (Google Cloud core)](https://docs.cloud.google.com/looker/docs/looker-core-overview) instance and you don't see your dialect listed in the **Dialect** drop-down menu, see the [Looker (Google Cloud core) documentation](https://docs.cloud.google.com/looker/docs/looker-core-dialects#supported_dialects_for) to verify that the dialect is supported for Looker (Google Cloud core) instances.
  3. Fill out the connection details. The majority of the settings are common to most database dialects. See the [Connecting Looker to your database](https://docs.cloud.google.com/looker/docs/connecting-to-your-db) documentation page for information.

  4. To verify that the connection is successful, click the **Test Connection** button in the **Status details** section at the bottom of the **Connections Settings** page.

  5. If Looker displays **Can Connect** , press **Connect** to create the connection. 




Your database connection is then added to the list on the Looker [**Connections**](https://docs.cloud.google.com/looker/docs/admin-panel-database-connections) **Admin** page.

## Supported JDBC parameters

For Exasol, Looker supports the following JDBC parameters in the [**Additional JDBC parameters**](https://docs.cloud.google.com/looker/docs/connecting-to-your-db#additional_jdbc_parameters) field for the connection. See the documentation for your database for information on these parameters.

  * `authmethod`
  * `autocommit`
  * `clientname`
  * `clientversion`
  * `connectionPoolSize`
  * `debug`
  * `enablenumerictypeconversion`
  * `encryption`
  * `feedbackinterval`
  * `fetchsize`
  * `fingerprint`
  * `hosttimeout`
  * `ignoreparams`
  * `kerberoshostname`
  * `kerberosservicename`
  * `legacyencryption`
  * `validateservercertificate`



## Feature support

For Looker to support some features, your database dialect must also support them.

Exasol supports the following features as of Looker 26.20:

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
