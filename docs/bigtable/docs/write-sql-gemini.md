---
url: https://docs.cloud.google.com/bigtable/docs/write-sql-gemini/
title: Write SQL with Gemini assistance \u00a0|\u00a0 Bigtable \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:50:30.901899+00:00
---

# Write SQL with Gemini assistance  |  Bigtable  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigtable/docs/write-sql-gemini/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Bigtable ](https://docs.cloud.google.com/bigtable/docs)
  * [ Guides ](https://docs.cloud.google.com/bigtable/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Write SQL with Gemini assistance

**Preview —[Gemini](https://docs.cloud.google.com/gemini/docs/overview) in Bigtable **

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This document describes how you can get AI-powered assistance with generating SQL queries using natural language prompts in Bigtable.

Learn [how and when Gemini for Google Cloud uses your data](https://docs.cloud.google.com/gemini/docs/discover/data-governance).

This document is intended for database administrators and data engineers who are familiar with Bigtable, SQL, and data analysis. If you're new to Bigtable, see [Quickstart: Create a Bigtable instance by using the Google Cloud console](https://docs.cloud.google.com/bigtable/docs/creating-instance-console).

## Limitations

  * You can't use Gemini in Bigtable to explain SQL queries in natural language.
  * Gemini in Bigtable might generate queries that are not valid in GoogleSQL for Bigtable or queries that use the following unsupported statements or syntax:

    * Data Manipulation Language (DML) statements other than `SELECT`—for example, `INSERT`, `UPDATE`, or `DELETE`.
    * Data Definition Language (DDL) statements—for example, `CREATE`, `ALTER`, or `DROP`.
    * Data access control statements.
    * Query syntax for subqueries, `JOIN`, `UNION`, and CTEs.

For more information, see [GoogleSQL for Bigtable overview](https://docs.cloud.google.com/bigtable/docs/googlesql-overview).




## Before you begin

  1. [Enable the Gemini for Google Cloud API in a Google Cloud project](https://docs.cloud.google.com/gemini/docs/codeassist/set-up-gemini#enable-api).

  2. To complete the tasks in this document, ensure that you have the necessary Identity and Access Management (IAM) permissions.

  3. Optional: If you want to follow along with the examples in this document, create and populate `test-table` as described in [Create a test table](https://docs.cloud.google.com/bigtable/docs/creating-test-table).




### Required roles

To get the permissions that you need to complete the tasks in this document, ask your administrator to grant you the [Gemini for Google Cloud User ](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudaicompanion#cloudaicompanion.user) (`roles/cloudaicompanion.user`) IAM role on the project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Generate SQL queries using natural language prompts

As an early-stage technology, Gemini for Google Cloud products can generate output that seems plausible but is factually incorrect. We recommend that you validate all output from Gemini for Google Cloud products before you use it. For more information, see [Gemini for Google Cloud and responsible AI](https://docs.cloud.google.com/gemini/docs/discover/responsible-ai).

You can give natural language comments (or _prompts_) to Gemini to generate queries that are based on your schema. For example, you can prompt Gemini to generate SQL in response to the following prompts:

  * "Count the number of devices that have a 1GB data plan."
  * "List all phones that were connected to Wifi on May 1st, 2019."
  * "Which tablets have the 10GB data plan enabled?"

**Note:** When you enter a prompt for Gemini in Bigtable, information about your database's schema is included with the prompt. This can include table and column names, data types, and column descriptions. Your database schema and data remain in Bigtable and aren't sent to Gemini.

To generate SQL in Bigtable with Gemini, follow these steps:

  1. In the Google Cloud console, go to the **Bigtable** page.

[Go to Bigtable](https://console.cloud.google.com/bigtable)

  2. Select an instance from the list.

  3. In the navigation pane, click **Bigtable Studio**.

  4. Open a new tab by clicking add, and then choose **Editor**.

  5. Click **Generate SQL**.

  6. In the **Help me code** dialog, enter your prompt, and then click **Generate**.

For example, if you enter the prompt `Count the number of devices that have a 1GB data plan.`, then Gemini generates SQL that's similar to the following:
         
         SELECT
             count(*)
         FROM
             `test_table`
         WHERE
             cell_plan['data_plan_01gb'] = 'true'
         

**Note:** Gemini might suggest different syntax each time that you enter the same prompt.
  7. Review the generated SQL and take one of the following actions:

     * To execute the suggested SQL, click **Insert** , and then click **Run**.
     * To edit the prompt, click **Edit** , and then click **Update**.
     * To edit the suggested SQL, click **Insert**. In the query builder, manually edit the query, and then click **Run**.
  8. Optional: To continue the `test_table` example, if you enter the prompt `Show all data for phones from May 2019.`, then Gemini generates SQL that is similar to the following:
         
         SELECT
             *
         FROM
             `test_table`
         WHERE
             _key LIKE 'phone#%#201905%'
         




## What's next

  * Read [Gemini for Google Cloud overview](https://docs.cloud.google.com/gemini/docs/overview).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
