---
url: https://docs.cloud.google.com/sql/docs/postgres/write-sql-gemini/
title: Write SQL with Gemini assistance \u00a0|\u00a0 Cloud SQL for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:29:48.908082+00:00
---

# Write SQL with Gemini assistance  |  Cloud SQL for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/postgres/write-sql-gemini/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ PostgreSQL ](https://docs.cloud.google.com/sql/docs/postgres)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/postgres/features)



Send feedback 

#  Write SQL with Gemini assistance Stay organized with collections  Save and categorize content based on your preferences. 

[MySQL](https://docs.cloud.google.com/sql/docs/mysql/write-sql-gemini "View this page for the MySQL database engine") | PostgreSQL | [SQL Server](https://docs.cloud.google.com/sql/docs/sqlserver/write-sql-gemini "View this page for the SQL Server database engine")

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). You can process personal data for this feature as outlined in the [Cloud Data Processing Addendum](https://docs.cloud.google.com/terms/data-processing-addendum), subject to the obligations and restrictions described in the agreement under which you access Google Cloud. Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This document describes how you can use [Gemini](https://docs.cloud.google.com/gemini/docs/overview), an AI-powered collaborator in Google Cloud, to help you do the following in Cloud SQL Studio:

  * Generate SQL queries using natural language prompts
  * Explain SQL queries in the query editor



Learn [how and when Gemini for Google Cloud uses your data](https://docs.cloud.google.com/gemini/docs/discover/data-governance).

This document is intended for database administrators and data engineers who are familiar with SQL, data analysis, and Cloud SQL. If you're new to Cloud SQL, see [Cloud SQL overview](https://docs.cloud.google.com/sql/docs/postgres/introduction).

## Before you begin

  1. To complete the tasks in this document, ensure that you have the necessary Identity and Access Management (IAM) permissions.
  2. Confirm access to Cloud SQL Studio. If you don't have access to Cloud SQL Studio, then see [Cloud SQL Studio required roles and permissions](https://docs.cloud.google.com/sql/docs/postgres/manage-data-using-studio#roles-and-permissions)
  3. Optional: To follow along with the examples in this document, create a `Singers` table using the following schema:
         
         CREATE TABLE
         Singers (
           SingerId   BIGINT PRIMARY KEY,
           FirstName  VARCHAR(1024),
           LastName   VARCHAR(1024),
           SingerInfo BYTEA,
           BirthDate  TIMESTAMPTZ
         );
         

After you create the `Singers` table, click refresh**Refresh** to update your database schema.




### Required roles and permissions

To get the permissions that you need to complete the tasks in this document, ask your administrator to grant you the [Cloud SQL Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudsql#cloudsql.admin) (`roles/cloudsql.admin`) IAM role on the project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

You also need the following permissions:

  * Either `serviceusage.services.list` or `serviceusage.services.get` permissions for read capabilities
  * `cloudaicompanion.companions.generateChat` permission to use explain SQL statements in the query editor
  * `cloudaicompanion.companions.generateCode` permission to use help me code



## Generate SQL queries using natural language prompts

As an early-stage technology, Gemini for Google Cloud products can generate output that seems plausible but is factually incorrect. We recommend that you validate all output from Gemini for Google Cloud products before you use it. For more information, see [Gemini for Google Cloud and responsible AI](https://docs.cloud.google.com/gemini/docs/discover/responsible-ai).

You can give Gemini natural language comments (or _prompts_) to generate queries that are based on your schema. For example, you can prompt Gemini to generate SQL in response to the following prompts:

  * "Add a date column called birthday to the Singers table."
  * "How many singers were born in the 90s?"



If your schema changes, such as addition of a new table or column, then click refresh**Refresh** to update your schema before using Gemini.

**Note:** When you enter a prompt for Gemini in Cloud SQL, information about your database's schema is included with the prompt. This metadata can include table and column names, data types, and column descriptions. Your database data remains in Cloud SQL and isn't sent to Gemini.

To generate SQL in Cloud SQL with Gemini assistance, follow these steps:

  1. In the Google Cloud console, go to the **Cloud SQL** page.

[Go to Cloud SQL](https://console.cloud.google.com/sql)

  2. Select an instance from the list.

  3. In the navigation menu, click **Cloud SQL Studio**.

  4. Sign in to Cloud SQL Studio using the name of your database, username, and password. The **Explorer** pane displays a list of objects in your database.

  5. In the taskbar, click settings_suggestionarrow_drop_down**Gemini** to view Gemini features in Cloud SQL.

  6. Ensure that **Comment-to-query generation** is enabled.

  7. To query your database, click add **New SQL editor tab**.

  8. To generate SQL, type a comment in the query editor starting with `--` followed by a [single-line comment](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/lexical#comments), and then press `Return` or `Enter`.

For example, enter the following prompt:
         
         -- add a row to table singers
         

Press `Return` or `Enter`. Gemini generates SQL that's similar to the following:
         
         INSERT INTO Singers (SingerId, FirstName, LastName, BirthDate)
         VALUES (1, 'Alex', 'M.', '1977-10-16');
         

To continue the example using the `Singers` table, enter the following prompt:
         
         -- show all singers born in the 70s
         

Gemini generates SQL that's similar to the following:
         
         SELECT *
         FROM Singers
         WHERE Singers.BirthDate
         BETWEEN '1970-01-01' AND '1979-12-31'
         
         

**Note:** Gemini might suggest different queries each time that you enter the same prompt.
  9. Review the SQL suggestion and take any of the following actions:

**Caution:** Because Data Manipulation Language (DML) and Data Definition Language (DDL) queries generated by Gemini can overwrite data, we recommend that you validate the generated queries before you run the queries.
     * To view the options for accepting the SQL generated by Gemini, hold the pointer over the query. The following options are displayed: 
       * **Accept** : To accept the suggested query, press `Tab`, then click **Run**.
       * **Accept word** : To accept the suggested query partially, press `Control`+`Right arrow`. (or `Command`+`Right arrow` on macOS), then click **Run**.
     * To edit the original SQL, press `Tab`, edit the SQL, and then click **Run**.
     * To dismiss the suggestion, press `Esc` or continue typing.



### Help me code tool

To use the **Help me code** tool, follow these steps:

  1. In the Google Cloud console, go to the **Cloud SQL** page.

[Go to Cloud SQL](https://console.cloud.google.com/sql)

  2. Select an instance from the list.

  3. In the navigation menu, click **Cloud SQL Studio**.

  4. Sign in to Cloud SQL Studio using the name of your database, username, and password. The **Explorer** pane displays a list of objects in your database.

  5. To query your database, click the add **New tab**.

  6. Click settings_suggestion **Help me code** next to the query editor.

  7. In the **Help me code** window, enter a prompt. For example, `add a row to table singers` and click **Generate**.

Gemini generates SQL that's similar to the following:
         
         INSERT INTO Singers (SingerId, FirstName, LastName, BirthDate)
         VALUES (1, Alex, 'M.', '1977-10-16');
         

**Note:** Gemini might suggest different syntax each time that you enter the same prompt.
  8. Review the generated SQL and take any of the following actions:

**Caution:** Because Data Manipulation Language (DML) and Data Definition Language (DDL) queries generated by Gemini can overwrite data, we recommend that you validate the generated queries before you run the queries.
     * To accept SQL generated by Gemini, click **Insert** to insert the statement into the query editor. Then click **Run** to execute the suggested SQL.
     * To ask Gemini to generate a new query, click **Edit**. After you've edited your prompt, click **Update**. You can then decide to accept the new generated statement or dismiss the suggestion.
     * To dismiss the suggestion, close the **Help me code** window.



## Explain SQL statements in the query editor

You can use Gemini in Cloud SQL to explain SQL queries in natural language. This explanation can help you understand the syntax, underlying schema, and business context for complex or long queries.

  1. In the Google Cloud console, go to the **Cloud SQL** page.

[Go to Cloud SQL](https://console.cloud.google.com/sql)

  2. Select an instance from the list.

  3. In the navigation menu, click **Cloud SQL Studio**.

  4. Sign in to Cloud SQL Studio using the name of your database, username, and password. The **Explorer** pane displays a list of objects in your database.

  5. To query your database, click the add **New tab**.

  6. In the query editor, paste the query you want explained.

  7. Highlight the query that you want Gemini to explain, and then click astrophotography_mode **Explain this selected query**.

The SQL explanation appears in the Gemini Cloud Assist pane.




## Use Gemini to fix errors in queries

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). You can process personal data for this feature as outlined in the [Cloud Data Processing Addendum](https://docs.cloud.google.com/terms/data-processing-addendum), subject to the obligations and restrictions described in the agreement under which you access Google Cloud. Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Gemini now offers an extended capability that helps you fix errors in your Cloud SQL queries without having to leave Cloud SQL Studio.

Gemini's AI-powered capabilities are integrated within Cloud SQL Studio to provide the following benefits:

  * Provides a line-for-line comparison of the original query next to a new query with recommended changes using the Cloud SQL Studio editor.
  * Highlights segments of the original query that might be causing the issue and provides a natural-language summary of changes.
  * References the exact error message and schema information associated with the query to provide accurate, relevant corrections.
  * Eliminates the need to rely on third-party, general-purpose LLMs that might provide less-nuanced help and might also expose your data to potential security risks.
  * Provides faster, more efficient troubleshooting for common issues such as syntax, schema, and runtime errors.



### Required permissions

Before you begin, confirm you have the following permissions:

  * The permissions outlined in [Required permissions](https://docs.cloud.google.com/sql/docs/postgres/write-sql-gemini#required-roles\)).
  * The Gemini for Google Cloud API permission, [`cloudaicompanion.googleapis.com/instances.generateCode`](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudaicompanion#cloudaicompanion.instances.generateCode).



### Fix your query using Gemini and Cloud SQL Studio

To use Gemini's capabilities to fix certain errors in a query in Cloud SQL Studio, complete the following:

  1. In the Google Cloud console, go to the **Cloud SQL** page.

[Go to Cloud SQL](https://console.cloud.google.com/sql)

  2. Select an instance from the list.

  3. In the navigation menu, click **Cloud SQL Studio**.

  4. Sign in to Cloud SQL Studio using the name of your database, username, and password. The **Explorer** pane displays a list of objects in your database.

  5. In the taskbar, click settings_suggestionarrow_drop_down**Gemini** to view Gemini features in Cloud SQL.

  6. To query your database, click the add **New tab**.

  7. In the query editor, enter a query that might be incorrect or incomplete.

  8. Click **Run**.

If the query contains an issue, an error is returned.

For example, the message returned might be a validation error in the **Run** tab, or an error message in the **Results** tab.

  9. Click **Fix**.

  10. In the query window, a differences editor ("diff editor") opens in the tab, showing a line-for-line comparison of the existing query with recommended changes. The query editor also provides a summary of the suggested edits. Review the suggested changes to the query and update as needed. Then, accept and run your new query:

Click **Accept and run**.




### Limitations

  * This capability is only accessible within Cloud SQL Studio in Google Cloud console.
  * Current [Gemini context window limits apply](https://ai.google.dev/gemini-api/docs/long-context#getting-started-with-long-context).



## What's next

  * Read [Gemini for Google Cloud overview](https://docs.cloud.google.com/gemini/docs/overview).
  * Learn [how Gemini uses your data](https://docs.cloud.google.com/gemini/docs/discover/data-governance). 
  * Learn how to [use Gemini conversational analytics to analyze your data](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics/sql-postgres). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
