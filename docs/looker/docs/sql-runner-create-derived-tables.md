---
url: https://docs.cloud.google.com/looker/docs/sql-runner-create-derived-tables/
title: Using SQL Runner to create derived tables \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:33:41.760270+00:00
---

# Using SQL Runner to create derived tables  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/sql-runner-create-derived-tables/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  Using SQL Runner to create derived tables Stay organized with collections  Save and categorize content based on your preferences. 

SQL Runner provides direct database access, which you can use to create and debug derived tables for your LookML projects. Use SQL Runner to define new derived tables and troubleshoot existing ones, helping you ensure data accuracy and improve your development workflow. This guide shows how to use SQL Runner for these tasks.

This page describes how to create a derived table using SQL Runner and how to use SQL Runner to debug derived tables. See these other documentation pages for information on:

  * [SQL Runner basics](https://docs.cloud.google.com/looker/docs/sql-runner-basics)
  * [Using SQL Runner to create queries and Explores](https://docs.cloud.google.com/looker/docs/sql-runner-create-queries-and-explores)
  * [Managing database functions with SQL Runner](https://docs.cloud.google.com/looker/docs/sql-runner-manage-db)



## Adding a SQL Runner query to a LookML project

SQL Runner is a great place to test SQL to use as a [derived table](https://docs.cloud.google.com/looker/docs/derived-tables) in your LookML project. You can even get a SQL query from a different tool, test it in SQL Runner, and then add it to your LookML project.

Once you have [created a SQL query in SQL Runner](https://docs.cloud.google.com/looker/docs/sql-runner-create-queries-and-explores), you can create a derived table from the query by using the **Add to Project** option or the **Get Derived Table LookML** option. Both of these options allow you to take a query in SQL Runner and add them to your LookML project. See the following sections for information.

### Add to Project

Using the **Add to Project** option is the easiest way to add a SQL Runner query to your project:

![SQL Runner page with the gear menu open and the Add to Project link highlighted.](https://docs.cloud.google.com/static/looker/docs/images/dev-sql-runner-add-to-project-2316.png)

The **Add to Project** option lets you select a LookML project, and then Looker automatically creates a [view file](https://docs.cloud.google.com/looker/docs/lookml-project-files#view_files) with the query in your selected project. If you would prefer instead to manually create the view file and add the query's LookML yourself, you can use the **Get Derived Table LookML** option.

Follow these steps to use the **Add to Project** option:

  1. Use SQL Runner to create a SQL query that you want to use for a derived table.
  2. Click **Add to Project** from the gear menu in the upper right.
  3. Select the project you want to add this derived table to.
  4. Enter a view name for the derived table.
  5. Click **Add** to add the query as a derived table in your project. Looker will switch to [Development Mode](https://docs.cloud.google.com/looker/docs/dev-mode-prod-mode) if not already in it, create a new view file with the LookML from the SQL Runner query, and then open the [IDE file browser](https://docs.cloud.google.com/looker/docs/ide-folders) to the new view file.
  6. [Move the file](https://docs.cloud.google.com/looker/docs/creating-project-files#moving_items_in_a_foldered_project) to suit your project's file organization.
  7. [Validate the LookML](https://docs.cloud.google.com/looker/docs/lookml-validation#validating_your_lookml) and [deploy your changes to production](https://docs.cloud.google.com/looker/docs/version-control-and-deploying-changes#getting_your_changes_to_production).



### Get Derived Table LookML

Another way to create a derived table from your SQL Runner query is to use the **Get Derived Table LookML** option from the SQL Runner gear menu. Just like with the **Add to Project** option, Looker will provide the LookML needed to make your SQL query into a derived table. From there, you can copy the LookML to paste into your project yourself, which is useful if you want to replace an existing derived table.

To create a derived table from a SQL Runner query:

  1. Use SQL Runner to create a SQL query that you want to use for a derived table.
  2. Click the gear menu and select **Get Derived Table LookML**.
  3. From the **Get Derived Table LookML** pop-up, click the **add it to your project** link.

**Note:** It's easier to use the **add it to your project** link, but you also have the option to copy the LookML, manually [create a view file](https://docs.cloud.google.com/looker/docs/creating-project-files#creating_files) in your project, and paste the LookML to your new view file.
  4. Use the drop-down **Project** list to choose the project you would like to add the derived table to.

  5. Enter a name for the new view in the **View Name** field. See the [Managing LookML files and folders](https://docs.cloud.google.com/looker/docs/creating-project-files#before_you_begin_important_file_and_folder_naming_conventions) page for file naming conventions.

  6. Click the **Add** button. Looker will switch to [Development Mode](https://docs.cloud.google.com/looker/docs/dev-mode-prod-mode) if not already in it, create a new view file with the LookML from the SQL Runner query, and then open the [IDE file browser](https://docs.cloud.google.com/looker/docs/ide-folders) to the new view file.

  7. [Move the file](https://docs.cloud.google.com/looker/docs/creating-project-files#moving_items_in_a_foldered_project) to suit your project's file organization.

  8. [Validate the LookML](https://docs.cloud.google.com/looker/docs/lookml-validation#validating_your_lookml) and [deploy your changes to production](https://docs.cloud.google.com/looker/docs/version-control-and-deploying-changes#getting_your_changes_to_production).




## Debugging using SQL Runner

SQL Runner is also a useful tool for checking SQL errors in the definition of a derived table.

### SQL Runner error highlighting

SQL Runner highlights the location of errors in the SQL command and includes the position of the error in the error message.

![](https://docs.cloud.google.com/static/looker/docs/images/dev-sql-runner-error-highlighting-512.png)

The position information provided will vary depending on the database dialect. For example, MySQL provides the line number that contains the error, while Redshift provides the character position of the error. Other database dialects might have one of these or other behaviors.

SQL Runner also highlights the location of the _first_ syntax error in the SQL command by underlining it in red and marking the row with an "x". Hover over the "x" to see more information on the error. After you fix that issue, click **Run** to see if there are any more errors in the query.

### Using SQL Runner to test derived tables

If you see an error coming from a derived table, you can determine the cause of the error by copying the SQL statement into SQL Runner and testing different parts of the SQL to narrow down the location of the error. For more information, see the [Using SQL Runner to test derived tables](https://discuss.google.dev/t/using-sql-runner-to-test-derived-tables/115142) Looker Community post.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-29 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-29 UTC."],[],[]] 
