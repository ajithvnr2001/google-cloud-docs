---
url: https://docs.cloud.google.com/alloydb/docs/security-best-practices/
title: Best practices for securing your AlloyDB for PostgreSQL resources \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T20:45:49.687309+00:00
---

# Best practices for securing your AlloyDB for PostgreSQL resources  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/docs/security-best-practices/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB for PostgreSQL ](https://docs.cloud.google.com/alloydb/docs)
  * [ Guides ](https://docs.cloud.google.com/alloydb/docs/overview)



Send feedback 

#  Best practices for securing your AlloyDB for PostgreSQL resources Stay organized with collections  Save and categorize content based on your preferences. 

To help you achieve a strong security posture for your AlloyDB for PostgreSQL resources, follow the best practices provided in this page.

## Prevent search path hijacking

To prevent [search path hijacking](https://wiki.postgresql.org/wiki/A_Guide_to_CVE-2018-1058%3A_Protect_Your_Search_Path), make sure that highly privileged users have the `search_path` parameter set to `pg_catalog`. This makes sure that the search path is secured and that untrusted schemas like `public` are bypassed.

To set this parameter permanently for a user, run the following command:
    
    
    ALTER ROLE USER_NAME SET search_path = pg_catalog,pg_temp;
    

To set this parameter only for the current session, run the following command:
    
    
    SET search_path TO pg_catalog,pg_temp;
    

To set this parameter for all users when connected to a database, run the following command:
    
    
    ALTER DATABASE DB_NAME SET search_path TO schema1, schema2, public;
    

For more information, see the [PostgreSQL documentation on secure schema usage](https://www.postgresql.org/docs/current/ddl-schemas.html#DDL-SCHEMAS-PATTERNS) and the [CVE-2018-1058 guide](https://wiki.postgresql.org/wiki/A_Guide_to_CVE-2018-1058%3A_Protect_Your_Search_Path).

## Secure BigQuery data access using the foreign data wrapper

When you use the BigQuery foreign data wrapper (FDW), all queries from AlloyDB to BigQuery are authenticated using the AlloyDB cluster's service account. Because this service account might have access to multiple sensitive BigQuery datasets, it's critical to prevent regular database users from mapping unauthorized tables.

To enforce least-privilege access, administrators must restrict `USAGE` privileges on the foreign server. This physically prevents non-administrator users from running `CREATE FOREIGN TABLE` statements.

  1. Restrict `USAGE` on the foreign server by ensuring that non-administrator roles don't have `USAGE` privileges on the foreign server. Revoke it from `PUBLIC` if necessary.
  2. Centralize table creation: Only database administrators, for example, users with the `alloydbsuperuser` role, can create foreign tables.
  3. Grant selective access: administrators manage read access by using `GRANT SELECT` on specific foreign tables.



### Example: Configuring Least-Privilege Access

The following workflow demonstrates how an administrator can securely grant a regular user (`bob`) access to a specific BigQuery table without allowing them to map arbitrary datasets.

\-- Step 1: Create the server and restrict access (Executed as Administrator) ```sql CREATE EXTENSION IF NOT EXISTS bigquery_fdw; CREATE SERVER bq_server FOREIGN DATA WRAPPER bigquery_fdw;

\-- Explicitly revoke USAGE from all users to prevent unauthorized table creation REVOKE ALL ON FOREIGN SERVER bq_server FROM PUBLIC; ```

\-- Step 2: Create a User Mapping for the regular user (Executed as Administrator) `sql CREATE USER MAPPING FOR bob SERVER bq_server;`

\-- Step 3: Create the Foreign Table (Executed as Administrator) \-- Because 'bob' does not have USAGE on bq_server, only the administrator can run this. `sql CREATE FOREIGN TABLE example_table ( id INT, state VARCHAR ) SERVER bq_server OPTIONS ( project 'BIGQUERY_PROJECT_ID', dataset 'BIGQUERY_DATASET_NAME', table 'example_table' );`

\-- Step 4: Grant Selective Read Access (Executed as Administrator) \-- Explicitly grant read access to the regular user for this specific table. `sql GRANT SELECT ON public.example_table TO bob;`

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
