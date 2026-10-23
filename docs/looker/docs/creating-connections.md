---
url: https://docs.cloud.google.com/looker/docs/creating-connections/
title: Creating connections tutorial \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:42:59.051139+00:00
---

# Creating connections tutorial  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/creating-connections/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  Creating connections tutorial Stay organized with collections  Save and categorize content based on your preferences. 

## General steps for creating a connection

The exact steps you need to take depend on the database dialect you are using and the other choices you make. This page serves as an outline of the steps you need to take to create a connection, with links to the details you need.

The steps are:

  1. From your database administrator, get the contact details for your database such as hostname, database or schema name, username, and password.

  2. Enable secure access to your database. There are two ways to do this:

     * Using an [IP address allowlist](https://docs.cloud.google.com/looker/docs/enabling-secure-db-access#option_1:_ip_address_allowlist), optionally adding [SSL encryption](https://docs.cloud.google.com/looker/docs/enabling-secure-db-access#option_2:_ssl_encryption).
     * Using an [SSH tunnel](https://docs.cloud.google.com/looker/docs/using-an-ssh-tunnel), which provides an encrypted connection and extra authentication. This is more secure but also is more time-consuming to set up.
  3. On your database, set it up to work with Looker. The instructions vary quite a bit from dialect to dialect. Typically the steps include adding permissions for Looker to access the database and possibly creating a scratch schema for Looker to create derived tables in the database. To see the instructions you need, go to the [Looker dialects](https://docs.cloud.google.com/looker/docs/dialects#setting_up_your_database) documentation page and click your database dialect.

  4. In Looker, go to the **Admin** panel's **Connection** page. If you are in a trial, typically you won't have any connections on that page.

  5. Click **Add Connection** to set up the connection. Fill out the connection details. The majority of the settings are common to most database dialects. See the [Connecting Looker to your database](https://docs.cloud.google.com/looker/docs/connecting-to-your-db) documentation page for information. In general, you specify the following values:

     * The name you want to use to refer to the connection
     * The database dialect
     * The connection information for reaching your database
     * Various options, including whether you'll let Looker write derived tables to the database and how you want the connection to behave
     * What time zone the database data is stored in
     * Additional JDBC connection string parameters, if needed by your database


  1. To verify that the connection is successful, click the **Test Connection** button in the **Status details** section at the bottom of the **Connections Settings** page.


  1. When the testing is successful, click **Connect**. The connection now appears on the **Admin** panel's **Connection** page. If you are in a trial, this will be your first connection on that page.

  2. Next, it is a good practice to double-check that your connection is working properly. In Looker, [use the **Develop** menu to go to SQL Runner](https://docs.cloud.google.com/looker/docs/sql-runner-basics#navigating_to_sql_runner), which lets you use a connection to do a variety of tasks such as directly typing and running SQL queries.

  3. In SQL Runner, select the name of the connection you created and the database or schema that you specified for the connection. Then check that the expected tables are listed. [Clicking a table](https://docs.cloud.google.com/looker/docs/sql-runner-manage-db#getting_table_information) will show the columns in that table, verifying that Looker was able to use the connection to access your database tables.




You have now set up the database connection and verified that Looker can reach the database.

## Next steps

If you are in a trial, your Looker analyst typically will have performed the other project setup steps for you. If you have time before your trial kickoff meeting, consider reading through the Development Process tutorials, which begin with the [Getting started developing in Looker](https://docs.cloud.google.com/looker/docs/data-modeling) documentation page, or consider the Looker courses on [Google Cloud Skills Boost](https://www.cloudskillsboost.google/paths/28).

If you are not in a trial, the next steps for creating a new project are:

  * [Creating a project](https://docs.cloud.google.com/looker/docs/generating-a-model) to hold your data model
  * [Configuring the project](https://docs.cloud.google.com/looker/docs/manage-projects#configuring_a_new_lookml_project) to accept your connection
  * [Setting up and testing Git](https://docs.cloud.google.com/looker/docs/setting-up-git-connection) to manage changes to the data model



Then you are ready to [start writing LookML](https://docs.cloud.google.com/looker/docs/what-is-lookml) and [deploying your changes to production](https://docs.cloud.google.com/looker/docs/version-control-and-deploying-changes#getting_your_changes_to_production) for your business users to do adhoc queries and create dashboards.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
