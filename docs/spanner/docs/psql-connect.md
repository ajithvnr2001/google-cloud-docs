---
url: https://docs.cloud.google.com/spanner/docs/psql-connect/
title: Connect psql to a PostgreSQL-dialect database \u00a0|\u00a0 Spanner \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:51:39.641827+00:00
---

# Connect psql to a PostgreSQL-dialect database  |  Spanner  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spanner/docs/psql-connect/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Spanner ](https://docs.cloud.google.com/spanner/docs)
  * [ Guides ](https://docs.cloud.google.com/spanner/docs/create-query-database-console)



Send feedback 

#  Connect psql to a PostgreSQL-dialect database Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to connect `psql` to a PostgreSQL-dialect database in Spanner. `psql` is the command-line front end to PostgreSQL.

  1. Ensure that PGAdapter is running on the same machine as the `psql` command.

For more information, see [Start PGAdapter](https://docs.cloud.google.com/spanner/docs/pgadapter-start).

  2. In a terminal window, start `psql` and specify `localhost` as the database server host.

     * Optionally specify a port number if PGAdapter is configured to listen on a port other than the default PostgreSQL port (5432).
     * Optionally specify one or more commands to send to the database or driver (for example, the JDBC driver). For each occurrence of the `-c` option, you can specify a single command or a batch of commands separated by semicolons (;). For more information, see [psql command-line tool](https://docs.cloud.google.com/spanner/docs/psql-commands).

`psql -h localhost [-p PORT] [-c "COMMAND; ..."] ...`

  3. Optional: Verify that `psql` successfully connected to a PostgreSQL-dialect database by submitting the following query:

`SELECT 1::bigint;`

This query is incompatible with GoogleSQL-dialect databases.




## What's next

  * Learn about [PGAdapter](https://docs.cloud.google.com/spanner/docs/pgadapter).
  * See the supported `psql` commands in [psql command-line tool](https://docs.cloud.google.com/spanner/docs/psql-commands).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
