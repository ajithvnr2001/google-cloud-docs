---
url: https://docs.cloud.google.com/alloydb/docs/write-sql-gemini/
title: Write SQL with Gemini assistance \u00a0|\u00a0 AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T20:46:09.581871+00:00
---

# Write SQL with Gemini assistance  |  AlloyDB for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/docs/write-sql-gemini/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB for PostgreSQL ](https://docs.cloud.google.com/alloydb/docs)
  * [ Guides ](https://docs.cloud.google.com/alloydb/docs/overview)



Send feedback 

#  Write SQL with Gemini assistance Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product is covered by the [Pre-GA Offerings Terms](https://cloud.google.com/terms/service-terms#0) of the Google Cloud Terms of Service. Pre-GA products might have limited support, and changes to pre-GA products might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This document describes how you can use [Gemini](https://docs.cloud.google.com/gemini/docs/overview), an AI-powered collaborator in Google Cloud, to help you do the following in AlloyDB for PostgreSQL:

  * Generate SQL queries using natural language prompts.
  * Explain SQL queries in the query editor.



Learn [how and when Gemini for Google Cloud uses your data](https://docs.cloud.google.com/gemini/docs/discover/data-governance).

This document is intended for database administrators and data engineers who are familiar with AlloyDB, and somewhat familiar with SQL and data analysis. If you're new to AlloyDB, see [AlloyDB overview](https://docs.cloud.google.com/alloydb/docs/overview).

## Before you begin

  1. [Ensure that Gemini Cloud Assist is set up for your Google Cloud user account and project](https://docs.cloud.google.com/cloud-assist/set-up-gemini).

  2. Optional: If you want to follow along with the examples in this document, create the `Singers` table using the following schema:
         
         CREATE TABLE Singers (
           BirthDate  TIMESTAMPTZ,
           SingerId   BIGINT PRIMARY KEY,
           FirstName  VARCHAR(1024),
           LastName   VARCHAR(1024),
           SingerInfo BYTEA
         );
         

After you create the `Singers` table, click refresh**Refresh** to update your database schema.




To disable Gemini features in AlloyDB, repeat this step, and then deselect the Gemini features that you want to disable.

### Required roles and permissions

**Caution:** Users with broad database access could experience data loss when using Gemini. We recommend that you use an account with fewer database privileges when using Gemini.

To use Gemini with AlloyDB, you need the following permissions:

  * `alloydb.clusters.get`
  * `alloydb.databases.list`
  * `alloydb.instances.executeSql`
  * `alloydb.instances.list`
  * `alloydb.users.list`
  * `cloudaicompanion.companions.generateCode`
  * `cloudaicompanion.instances.generateCode`
  * `serviceusage.services.get` or `serviceusage.services.list`



You can get this permission through the [`roles/alloydb.admin`](https://docs.cloud.google.com/alloydb/docs/reference/iam-roles-permissions#roles) role. If you don't have this role, contact your Organization Administrator to request access. You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/understanding-roles).

Additionally, ensure that you have [database-level permissions](https://docs.cloud.google.com/alloydb/docs/database-users/about) for the database that you're using for authentication.

## Generate SQL queries using natural language prompts

As an early-stage technology, Gemini for Google Cloud products can generate output that seems plausible but is factually incorrect. We recommend that you validate all output from Gemini for Google Cloud products before you use it. For more information, see [Gemini for Google Cloud and responsible AI](https://docs.cloud.google.com/gemini/docs/discover/responsible-ai).

You can give Gemini natural language comments (or _prompts_) to generate queries that are based on your schema. For example, you can prompt Gemini to generate SQL in response to the following prompts:

  * "Create a table that tracks customer satisfaction survey results."
  * "Add a date column called birthday to the Singers table."
  * "How many singers were born in the 90s?"



If your schema changes, such as addition of a new table or column, then you must click refresh**Refresh** to update your schema before using Gemini.

**Note:** When you enter a prompt, information about your database's schema is included with the prompt. This can include table and column names, data types, and column descriptions. Your database schema and data remain in AlloyDB and aren't sent to Gemini.

To generate SQL in AlloyDB with Gemini assistance, follow these steps:

  1. In the Google Cloud console, open the **AlloyDB** page.

[Go to AlloyDB](https://console.cloud.google.com/alloydb)

  2. Select a cluster from the list.

  3. In the navigation menu, click **AlloyDB**.

  4. Select a database and user, and enter the user's password.

  5. Click **Authenticate**. The **Explorer** pane displays a list of the objects in your database.

  6. To query your database, click the add **New SQL editor tab**. Make sure that SQL generation is enabled.

  7. To generate SQL, type a comment in the query editor starting with `--` followed by a [single-line comment](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/lexical#comments), and then press `Return`.

For example, if you enter the prompt `-- add a row to table singers` and press `Return`, then Gemini generates SQL that's similar to the following:
         
         INSERT INTO Singers (SingerId, FirstName, LastName, BirthDate)
         VALUES (1, Alex, 'M.', '1977-10-16');
         

To continue the example using the `Singers` table, if you enter the prompt `-- show all singers born in the 70s`, then Gemini generates SQL that's similar to the following:
         
         SELECT *
         FROM Singers
         WHERE Singers.BirthDate
         BETWEEN '1970-01-01' AND '1979-12-31'
         

**Note:** Gemini might suggest different syntax each time that you enter the same prompt.
  8. Review the SQL suggestion and take any of the following actions:

**Caution:** Because Data Manipulation Language (DML) and Data Definition Language (DDL) queries generated by Gemini can overwrite data, we recommend that you validate the generated SQL queries before you run the queries.
     * To view the options for accepting the SQL generated by Gemini, hold the pointer over the query. The following options are displayed: 
       * **Accept** : To accept the suggested query, press `Tab`, then click **Run**.
       * **Accept word** : To accept the suggested query partially, press `Control`+`Right arrow`. (or `Command`+`Right arrow` on macOS), then click **Run**.
     * To edit the original SQL, press `Tab`, edit the SQL, and then click **Run**.
     * To dismiss the suggestion, press `Esc` or continue typing.



### Help me code tool

To use the **Help me code** tool, follow these steps:

  1. In the Google Cloud console, open the **AlloyDB** page.

[Go to AlloyDB](https://console.cloud.google.com/alloydb)

  2. Select a cluster from the list.

  3. In the navigation menu, click **AlloyDB**.

  4. Select a database and user, and enter the user's password.

  5. Click **Authenticate**. The **Explorer** pane displays a list of the objects in your database.

  6. To query your database, click the add **New tab**.

  7. Click pen_spark **Help me code** next to the query editor.

  8. In the **Help me code** window, enter a prompt. For example, `add a row to table singers` and click **Generate**.

Gemini generates SQL that's similar to the following:
         
         INSERT INTO Singers (SingerId, FirstName, LastName, BirthDate)
         VALUES (1, Alex, 'M.', '1977-10-16');
         

**Note:** Gemini might suggest different syntax each time that you enter the same prompt.
  9. Review the generated SQL and take any of the following actions:

**Caution:** Because Data Manipulation Language (DML) and Data Definition Language (DDL) queries generated by Gemini can overwrite data, we recommend that you validate the generated queries before you run the queries.
     * To accept SQL generated by Gemini, click **Insert** to insert the statement into the query editor. Then click **Run** to execute the suggested SQL.
     * To ask Gemini to generate a new query, click **Edit**. After you've edited your prompt, click **Update**. You can then decide to accept the new generated statement or dismiss the suggestion.
     * To dismiss the suggestion, close the **Help me code** window.



## Explain SQL statements in the query editor

You can enter natural language queries to request explanations of SQL queries. These explanations can help you understand the syntax, underlying schema, and business context for complex or long queries.

  1. In the Google Cloud console, open the **AlloyDB** page.

[Go to AlloyDB](https://console.cloud.google.com/alloydb)

  2. Select a cluster from the list.

  3. In the navigation menu, click **AlloyDB**.

  4. Select a database and user, and enter the user's password.

  5. Click **Authenticate**. The **Explorer** pane displays a list of the objects in your database.

  6. To query your database, click the add **New tab**.

  7. In the query editor, paste the query.

  8. Highlight the query that you want Gemini to explain, and then click astrophotography_mode **Explain this selected query**.

The SQL explanation appears in the Gemini Cloud Assist pane.




## Use Gemini to fix errors in queries

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). You can process personal data for this feature as outlined in the [Cloud Data Processing Addendum](https://docs.cloud.google.com/terms/data-processing-addendum), subject to the obligations and restrictions described in the agreement under which you access Google Cloud. Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Gemini offers an extended capability that helps you fix errors in your AlloyDB queries without having to leave the query editor.

Gemini's AI-powered capabilities are integrated within the query editor to provide the following benefits:

  * Provides a line-for-line comparison of the original query next to a new query with recommended changes using the query editor.
  * Highlights segments of the original query that might be causing the issue and provides a natural-language summary of changes.
  * References the exact error message and schema information associated with the query to provide accurate, relevant corrections.
  * Eliminates the need to rely on third-party, general-purpose LLMs that might provide less-nuanced help and might also expose your data to potential security risks.
  * Provides faster, more efficient troubleshooting for common issues such as syntax, schema, and runtime errors.



### Required permissions

Before you begin, confirm you have the following permissions:

  * The permissions outlined in [Required permissions](https://docs.cloud.google.com/alloydb/docs/write-sql-gemini#required-roles).
  * The Gemini for Google Cloud API permission, [`cloudaicompanion.googleapis.com/instances.generateCode`](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudaicompanion#cloudaicompanion.instances.generateCode).



### Fix your query using Gemini

To use Gemini's capabilities to fix certain errors in a query, complete the following:

  1. In the Google Cloud console, open the **AlloyDB for PostgreSQL** page.

[Go to AlloyDB](https://console.cloud.google.com/alloydb)

  2. Select a cluster from the list.

  3. In the navigation menu, click **AlloyDB Studio**.

  4. Select a database and user, and enter the user's password.

  5. Click **Authenticate**. The **Explorer** pane displays a list of the objects in your database.

  6. In the taskbar, click settings_suggestionarrow_drop_down**Gemini** to view Gemini features in AlloyDB.

  7. To query your database, click add **New tab**.

  8. In the query editor, enter a query that might be incorrect or incomplete.

  9. Click **Run**.

If the query contains an issue, an error is returned in the **Results** tab.

  10. Click **Fix**.

In the query window, a differences editor ("diff editor") opens in the tab, showing a line-for-line comparison of the existing query with recommended changes. The query editor also provides a summary of the suggested edits.

  11. Review the suggested changes to the query and update as needed. 

  12. To accept the changes and run your new query, click **Accept and run**.




### Limitations

  * This capability is only accessible in AlloyDB Studio query editor in Google Cloud console.
  * Current [Gemini context window limits apply](https://ai.google.dev/gemini-api/docs/long-context#getting-started-with-long-context).



## What's next

  * Read [Gemini for Google Cloud overview](https://docs.cloud.google.com/gemini/docs/overview).
  * Learn [how Gemini uses your data](https://docs.cloud.google.com/gemini/docs/discover/data-governance).
  * Learn how to [analyze your data in Google Cloud using Gemini](https://docs.cloud.google.com/bigquery/docs/gemini-analyze-data).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
